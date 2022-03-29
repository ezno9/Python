# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.
#
# 입출력 예
# n	    computers	                        return
# 3	    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	    [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

def solution(n, computers):
    answer = 0                  # 네트워크의 개수를 저장할 변수
    bfs = []                    # 탐색을 위한 큐
    visited = [0]*n             # 방문한 노드를 체크해 둘 리스트

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)               # 큐에 첫 노드(인덱스) 추가
        visited[x] = 1              # 첫 노드 방문 표시

        while bfs:                  # 큐가 값이 존재하면 반복문 실행
            node = bfs.pop(0)       # 큐의 앞에서부터 노드(인덱스) 꺼내기
            visited[node] = 1
            for i in range(n):      # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
                if visited[i] == 0 and computers[node][i] == 1:
                                    # 인접 노드이고, 방문된 적이 없는 경우
                    bfs.append(i)   # 큐에 추가
                    visited[i] == 1 # 방문했음을 표시
        answer += 1
    return answer

print('결과1 : ', solution(3, [[1,1,0], [1,1,0], [0,0,1]]))
print('결과2 : ', solution(3, [[1,1,0], [1,1,1], [0,1,1]]))


def dfs(x, computers):
    computers[x][x] = 2 # 들린거 표시
    for i in range(len(computers[x])):
        if computers[x][i]==1 and computers[i][i]!=2: # 처음 들리는 곳이면
            dfs(i,computers)

def solution(n, computers):
    answer = 0

    for i in range(n):
        if computers[i][i]==1:
            dfs(i, computers)
            answer += 1
    return answer

print('결과3 : ', solution(3, [[1,1,0], [1,1,0], [0,0,1]]))
print('결과4 : ', solution(3, [[1,1,0], [1,1,1], [0,1,1]]))




