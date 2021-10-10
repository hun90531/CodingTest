def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1단계

    # 2단계
    for s in new_id:
        if '0' <= s <= '9' or 'a' <= s <= 'z' or s == '-' or s == '_' or s == '.':
            answer = answer + s

    # 3단계
    for i in range(len(answer), 1, -1):
        del_str = '.' * i
        answer = answer.replace(del_str, '.')

    # 4단계
    i = 0
    while i < len(answer) and answer[i] == '.':
        i = i + 1

    j = len(answer) - 1
    while j >= 0 and answer[j] == '.':
        j = j - 1

    answer = answer[i: j + 1]

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) < 3:
        return answer + answer[-1] * (3 - len(answer))

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))

print(solution("z-+.^."))

print(solution("=.="))

print(solution("123_.def"))

print(solution("abcdefghijklmn.p"))

print(solution('.............................'))