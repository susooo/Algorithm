def solution(expressions):
    def cal(num, base):
        result = 0
        for digit in num:
            result = result * base + int(digit)
        return result

    def re_cal(num, base):
        if num == 0:
            return "0"
        digits = ""
        while num > 0:
            digits = str(num % base) + digits
            num //= base
        return digits

    def is_valid_in_base(s, base):
        return all(int(ch) < base for ch in s)

    problems = []
    avail = []

    for base in range(2, 10):
        valid = True
        for expr in expressions:
            n1, op, n2, eq, an = expr.split()

            if not (is_valid_in_base(n1, base) and is_valid_in_base(n2, base)):
                valid = False
                break
            if an != "X" and not is_valid_in_base(an, base):
                valid = False
                break

            first = cal(n1, base)
            second = cal(n2, base)

            if an == "X":
                continue
            result = cal(an, base)

            if op == "+" and first + second != result:
                valid = False
                break
            if op == "-" and first - second != result:
                valid = False
                break

        if valid:
            avail.append(base)

    # collect problems
    for expr in expressions:
        if expr.split()[-1] == "X":
            problems.append(expr)

    # solve unknowns
    answer = []
    for expr in problems:
        n1, op, n2, eq, _ = expr.split()
        possible_results = set()
        for base in avail:
            first = cal(n1, base)
            second = cal(n2, base)
            res = first + second if op == "+" else first - second
            res_str = re_cal(res, base)
            possible_results.add(res_str)

        if len(possible_results) == 1:
            answer.append(f"{n1} {op} {n2} {eq} {possible_results.pop()}")
        else:
            answer.append(f"{n1} {op} {n2} {eq} ?")

    return answer