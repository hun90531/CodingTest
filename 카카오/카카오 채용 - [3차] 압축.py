def solution(msg):
    answer = []
    dic = {}
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = i - ord('A') + 1

    m = 26
    i = 0
    while True:
        j = i + 1
        # 사전에 없는게 나올때까지 j 더하기
        while j <= len(msg) and msg[i:j] in dic:
            j = j + 1

        m = m + 1

        # while 문이 종료된 이유가
        # msg[i:j]가 사전에 없기때문이라면
        if msg[i:j] not in dic:
            dic[msg[i:j]] = m

        # 사전에 추가한 단어에서 한 글자 뺀걸 출력해야 한다.
        answer.append(dic[msg[i:j - 1]])
        i = j - 1

        if i >= len(msg):
            break

    return answer

print(solution('KAKAO'))

print(solution('TOBEORNOTTOBEORTOBEORNOT'))

print(solution('ABABABABABABABAB'))