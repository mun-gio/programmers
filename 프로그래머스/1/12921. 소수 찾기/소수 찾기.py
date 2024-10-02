def solution(n):
    # 소수 여부를 저장할 리스트 초기화
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  # i가 소수일 경우
            for j in range(i * i, n + 1, i):
                is_prime[j] = False  # i의 배수는 소수가 아님
    
    # 소수 개수 세기
    return sum(is_prime)