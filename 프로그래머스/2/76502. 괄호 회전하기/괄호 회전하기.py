def solution(s):
    answer = 0
    for i in s:
        stack = []
        for p in range(len(s)):
            if s[p] == "(":
                stack.append(")")
            elif s[p] == "[":
                stack.append("]")
            elif s[p] == "{":
                stack.append("}")
            elif stack and stack[-1] == s[p]:
                stack.pop()
                if p+1 == len(s) and not stack:
                    answer += 1
            else:
                break
        s = s[1:]+s[:1]
    return answer