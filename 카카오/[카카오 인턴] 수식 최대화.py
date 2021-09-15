import sys
from itertools import permutations

input = sys.stdin.readline


def solution(expression):
    operator = ['*', '+', '-']
    permutation = permutations(operator, 3)

    oper = []  # 연산자 저장
    num = []  # 숫자 저장
    res = []  # 결과 모음

    n = ''
    for i in expression:
        if i in operator:
            oper.append(i)
            num.append(n)
            n = ''
        else:
            n = n + i
    else:
        num.append(n)

    for op in permutation:
        temp_oper = oper[:]
        temp_num = num[:]
        for o in op:
            # 연산자는 o에 대해서 계산할 예정
            while o in temp_oper:
                index = temp_oper.index(o)
                cal = temp_num[index] + o + temp_num[index + 1]
                temp_num[index + 1] = str(eval(cal))
                temp_num.pop(index)
                temp_oper.pop(index)

        res.append(abs(int(temp_num[0])))

    return max(res)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))