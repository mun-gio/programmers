def solution(n):
    answer = ""
    st = []
    for i in range(len(str(n))):
        st.append((n//10**i)-(n//10**(i+1)*10))
    st.sort(reverse=True)
    for i in st:
        answer += str(i)
    return int(answer)