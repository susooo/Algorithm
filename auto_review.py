from dotenv import load_dotenv
load_dotenv()

import json, os
from pathlib import Path
from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from github import Github

# ── 1) LLM 클라이언트 ────────────────────────────────
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# ── 2) 공유 State 정의 ────────────────────────────────
# 모든 노드가 이 State를 읽고 업데이트함
class ReviewState(TypedDict):
    filepath: str           # 입력
    problem_title: str      # 입력: 문제 이름
    problem_desc: str       # 입력: 문제 설명
    solution: str           # 입력: 내 풀이 코드
    language: str           # 입력: Python / Java 등

    analysis: dict          # code_analyzer 가 채워줌
    history: dict           # solution_intake / weakness_tracker 가 채워줌
    feedback: str           # feedback_generator 가 채워줌
    recommendations: List[str]  # problem_recommender 가 채워줌
    review_text: str            # output_formatter 가 채워줌

# 히스토리 로드/저장
HISTORY_FILE = Path("history.json")

# ── 히스토리 로드/저장 ────────────────────────────────
def load_history() -> dict:
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    return {"weak_topics": {}, "solved_by_algorithm": {}, "total": 0}

def save_history(h: dict):
    HISTORY_FILE.write_text(
        json.dumps(h, ensure_ascii=False, indent=2), #ident: 들여쓰기 옵션
        encoding="utf-8"
    )

# ── 3) 노드 정의 ─────────────────────────────────────
# State = 노드들이 공유하는 메모장, 처음에 내 풀이를 넣고 노드마다 결과가 채워짐

def file_loader(state: ReviewState) -> dict:
    #히스토리 로드
    filepath = state["filepath"]
    solution = Path(filepath).read_text(encoding="utf-8")

    readme_path = Path(filepath).parent / "README.md"
    problem_desc = readme_path.read_text(encoding="utf-8") if readme_path.exists() else "설명 없음"

    problem_title = Path(filepath).parent.name.replace("_", " ")

    ext_map = {".py": "Python", ".java": "Java", ".js": "JavaScript"}
    language = ext_map.get(Path(filepath).suffix, "Python")

    return {
        "problem_title": problem_title,
        "problem_desc": problem_desc,
        "solution": solution,
        "language": language,
        "history": load_history(),
    }
    
def code_analyzer(state: ReviewState) -> dict:
    prompt = f"""You are a coding interview expert. Analyze this solution.
IMPORTANT: All values in hidden_cases must be written in Korean.

Problem: {state['problem_title']}
Description: {state['problem_desc']}
Language: {state['language']}
Solution:
{state['solution']}

Respond ONLY in this JSON format:
{{
"my_algorithm": "알고리즘 이름만",
"time_complexity": "O(?)",
"optimal_algorithm": "알고리즘 이름만",
"optimal_time_complexity": "O(?)",
"correctness": "correct / partial / incorrect",
"hidden_cases": [
    {{
      "case": "히든 케이스 설명 (한국어)",
      "reason": "왜 이 케이스에서 틀리는지 (한국어)",
      "lesson": "앞으로 이런 문제에서 고려할 점 (한국어)"
    }}
  ],
"weak_topic": "main weak topic"
}}"""

    resp = llm.invoke(prompt)   # Gemini API 호출

    # 응답에서 JSON 파싱
    try:
        text = resp.content.strip()
        if "```" in text:
            text = text.split("```")[1].replace("json","").strip()
        analysis = json.loads(text)
    except:
        analysis = {
            "my_algorithm": "?",
            "time_complexity": "?",
            "optimal_algorithm": "?",
            "optimal_time_complexity": "?",
            "correctness": "unknown",
            "hidden_cases": [],
            "weak_topic": "Unknown"
        }
    return {"analysis": analysis}

# 약점유형 누적 저장: 틀린 문제만 약점으로 누적 + 알고리즘별 분류하여 history.json에 카운트 쌓기
def weakness_tracker(state: ReviewState) -> dict:
    h = state["history"]
    analysis = state["analysis"]
    topic = state["analysis"].get("weak_topic", "Unknown")
    correctness = analysis.get("correctness", "unknown")
    my_algorithm = analysis.get("my_algorithm", "Unknown")
    problem_title = state["problem_title"]
    
    # partial / incorrect일 때만 약점 카운트
    if correctness in ("partial", "incorrect"):
        h["weak_topics"][topic] = h["weak_topics"].get(topic, 0) + 1

    # 알고리즘별 분류 저장
    if my_algorithm not in h["solved_by_algorithm"]:
        h["solved_by_algorithm"][my_algorithm] = []
        
    # 중복 방지
    if problem_title not in h["solved_by_algorithm"][my_algorithm]:
        h["solved_by_algorithm"][my_algorithm].append(problem_title)

    h["total"] += 1
    save_history(h)
    return {"history": h}

# 피드백: 풀이 코드 + 분석 결과를 보내서 한국어 피드백을 받기
def feedback_generator(state: ReviewState) -> dict:
    analysis = state["analysis"]
    correctness = analysis.get("correctness", "unknown")
    
    tone = {
        "correct":   "풀이가 정확합니다. 최적화 관점에서 피드백해주세요.",
        "partial":   "일부 케이스에서 틀렸습니다. 개선점을 중점적으로 피드백해주세요.",
        "incorrect": "풀이가 틀렸습니다. 문제점을 명확히 짚어주세요.",
    }.get(correctness, "")
    
    prompt = f"""You are a coding mentor. Give feedback in Korean.

Problem: {state['problem_title']}
My solution: {state['solution']}
Analysis:
- My algorithm: {analysis.get('my_algorithm')}
- Time complexity: {analysis.get('time_complexity')}
- Optimal algorithm: {analysis.get('optimal_algorithm')}
- Optimal complexity: {analysis.get('optimal_time_complexity')}

Provide feedback in this structure:
1. 잘한 점 (1-2줄)
2. 개선할 점 (1-2줄)
3. 최적 접근법 힌트 (코드 말고 힌트만)
4. 시간복잡도 개선 방향

Keep it concise. Use Korean."""

    resp = llm.invoke(prompt)
    return {"feedback": resp.content}

#문제 추천: 약점 통계를 보내서 다음 문제 3개를 추천받기
def recommendation_generator(state: ReviewState) -> dict:
    h = state["history"]
    top_weak = sorted(h["weak_topics"].items(), key=lambda x: -x[1])[:3]
    weak_str = ", ".join([f"{t}({c}회 틀림)" for t, c in top_weak]) or "아직 없음"

    prompt = f"""You are a coding test coach. Recommend next Programmers problems in Korean.

Student's weak topics (틀린 횟수 기준): {weak_str}
Total solved: {h['total']}
Current problem weak topic: {state['analysis'].get('weak_topic')}
Current problem correctness: {state['analysis'].get('correctness')}

Recommend exactly 3 Programmers(프로그래머스) problems.
IMPORTANT: Only recommend problems that are Level 2 or higher (레벨 2 이상).
Format (strictly follow this):
1️⃣  [문제이름] - 추천 이유 한 줄
2️⃣  [문제이름] - 추천 이유 한 줄
3️⃣  [문제이름] - 추천 이유 한 줄

Focus on the weakest topics."""

    resp = llm.invoke(prompt)
    lines = [l.strip() for l in resp.content.split("\n") if l.strip()]
    return {"recommendations": lines}

# ── 4) 결과 출력 ─────────────────────────────────────
#State 에 쌓인 모든 결과를 모아서 터미널에 출력하기
def review_formatter(state: ReviewState) -> dict:
    analysis = state["analysis"]
    h = state["history"]
    correctness = analysis.get("correctness", "unknown")
    
    correctness_emoji = {
        "correct":   "✅ 정답",
        "partial":   "🟡 부분 정답",
        "incorrect": "❌ 오답",
    }.get(correctness, "❓ 알 수 없음")
    
    my_algo = analysis.get('my_algorithm', '?')
    optimal_algo = analysis.get('optimal_algorithm', '?')
    my_time = analysis.get('time_complexity', '?')
    optimal_time = analysis.get('optimal_time_complexity', '?')
    
    #히든 케이스
    hidden_cases = analysis.get('hidden_cases', [])
    hidden_str = ""
    for hc in hidden_cases:
        hidden_str += f"""  ▪ **{hc.get('case', '')}**
     └ 이유: {hc.get('reason', '')}\n
     └ 학습: {hc.get('lesson', '')}\n\n"""
    
    # 추천 문제
    rec_str = "\n".join(state["recommendations"]) if state["recommendations"] else "추천 문제 없음"
    
    review_text = f"""

## 🤖 AI 코드 리뷰 — {state['problem_title']}

### 🧠 알고리즘 비교 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
| | 알고리즘 | 시간복잡도 |
|---|---|---|
| 내 풀이 | {analysis.get('my_algorithm', '?')} | {analysis.get('time_complexity', '?')} |
| 최적 풀이 | {analysis.get('optimal_algorithm', '?')} | {analysis.get('optimal_time_complexity', '?')} |

### 💬 피드백 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
{state['feedback']}

### 🕵️ 히든 케이스 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
{hidden_str if hidden_str else "특이한 히든 케이스 없음"}

### 📚 다음 추천 문제 ━━━━━━━━━━━━━━━━━━━━━━━━━━━
{rec_str}
"""

    return {"review_text": review_text}

def github_poster(state: ReviewState) -> dict:
    # GitHub 커밋 코멘트 게시
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(os.environ["REPO_NAME"])
    commit = repo.get_commit(os.environ["COMMIT_SHA"])
    commit.create_comment(state["review_text"])
    print(f"✅ {state['problem_title']} 리뷰 게시 완료!")
    return {}

# ── 5) 그래프 조립 ───────────────────────────────────
def build_graph():
    g = StateGraph(ReviewState)

    # 노드 등록
    g.add_node("file_loader",              file_loader)
    g.add_node("code_analyzer",            code_analyzer)
    g.add_node("weakness_tracker",         weakness_tracker)
    g.add_node("feedback_generator",       feedback_generator)
    g.add_node("recommendation_generator", recommendation_generator)
    g.add_node("review_formatter",         review_formatter)
    g.add_node("github_poster",            github_poster)

    # 엣지 연결
    g.add_edge(START,                  "file_loader")
    g.add_edge("file_loader",          "code_analyzer")
    g.add_edge("code_analyzer",       "weakness_tracker")
    g.add_edge("weakness_tracker",    "feedback_generator")
    g.add_edge("weakness_tracker",    "recommendation_generator")
    g.add_edge("feedback_generator",        "review_formatter")
    g.add_edge("recommendation_generator",  "review_formatter")
    g.add_edge("review_formatter",          "github_poster")
    g.add_edge("github_poster",             END)

    return g.compile()

# ── 6) 실행 ──────────────────────────────────────────
def parse_changed_files():
    from pathlib import Path

    file = Path("changed_files.txt")
    
    if not file.exists():
        return []

    content = file.read_text(encoding="utf-8")
    files = [
        line.strip()
        for line in content.splitlines()
        if line.strip().endswith(".py")
    ]

    return files

if __name__ == "__main__":
    files = parse_changed_files()
    
    if not files:
        print("분석할 파일 없음")
        exit(0)
    
    app = build_graph()
    for filepath in files:
        print(f"🚀 분석 시작: {filepath}")
        app.invoke({
            "filepath": filepath,
            "problem_title": "",
            "problem_desc": "",
            "solution": "",
            "language": "",
            "history": {},
            "analysis": {},
            "feedback": "",
            "recommendations": [],
            "review_text": "",
        })
