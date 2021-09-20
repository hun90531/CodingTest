from collections import deque

'''
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0],
[1, 0, 0, 0, 1],
[0, 1, 1, 0, 0]

와 같이 같은 위치에 비용이 더 높은 경우지만
장기적으로 점점 더 낮은 비용의 결과가 발생하는 경우가 있기 때문에
동쪽으로 출발하는 경우와 남쪽으로 출발하는 경우를 나눠서 실행해야 한다.    
'''

def solution(board):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    length = len(board)

    def bfs(direct):
        arr = board[:]
        dq = deque()
        dq.append([0, 0, 0, direct])  # i, j, 비용, 방향

        while dq:
            i, j, cost, d = dq.popleft()
            if arr[i][j] == 1:
                continue

            if i == length - 1 and j == length - 1:
                continue

            # 동서남북 방향 => 동서남북 : 0 1 2 3
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]

                if 0 <= ni < length and 0 <= nj < length:
                    if ni == 0 and nj == 0:
                        continue

                    if d == dir:
                        fee = 100
                    else:
                        fee = 600

                    if arr[ni][nj] == 0 or arr[ni][nj] >= cost + fee:
                        arr[ni][nj] = cost + fee
                        dq.append([ni, nj, cost + fee, dir])

        return board[-1][-1]

    return min(bfs(0), bfs(2))


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
      )

print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0],
                [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
      )

# 14번 테스트케이스
print(solution([
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]))

# 25번 테스트케이스
print(solution([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0]])
)