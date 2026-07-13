def solution(k, room_number):
    answer = []
    parent = {}
    
    def find(x):
        # 루트 찾기
        root = x
        while root in parent:
            root = parent[root]
        
        # 경로 압축 (x에서 root까지 모두 root로 연결)
        while x in parent:
            parent[x], x = root, parent[x]
            
        return root

    for num in room_number:
        room = find(num)
        answer.append(room)
        parent[room] = room+1
        
    return answer