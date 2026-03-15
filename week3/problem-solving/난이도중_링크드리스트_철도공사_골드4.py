# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 기존 풀이 -> 배열로 처리
import sys
input = sys.stdin.readline

MAX = 1000001
prev_arr = [0] * MAX
next_arr = [0] * MAX
alive = [False] * MAX  # station_nums 역할 (존재 여부)
result = []

def append_station(tail, data):
    if not tail:
        prev_arr[data] = data
        next_arr[data] = data
        alive[data] = True
        return data

    head = next_arr[tail]

    prev_arr[data] = tail
    next_arr[data] = head

    next_arr[tail] = data
    prev_arr[head] = data

    alive[data] = True
    return data  # 새 tail

def run_bn(i, j):
    # i+1 출력, i - j - (i+1) 삽입
    result.append(str(next_arr[i]))
    nxt = next_arr[i]

    next_arr[i] = j
    prev_arr[j] = i
    next_arr[j] = nxt
    prev_arr[nxt] = j

    alive[j] = True

def run_bp(i, j):
    # i-1 출력, (i-1) - j - i 삽입
    result.append(str(prev_arr[i]))
    prv = prev_arr[i]

    prev_arr[i] = j
    next_arr[j] = i
    prev_arr[j] = prv
    next_arr[prv] = j

    alive[j] = True

def run_cn(i):
    # i+1 폐쇄 후 출력
    target = next_arr[i]
    result.append(str(target))

    nxt = next_arr[target]
    next_arr[i] = nxt
    prev_arr[nxt] = i

    alive[target] = False

def run_cp(i):
    # i-1 폐쇄 후 출력
    target = prev_arr[i]
    result.append(str(target))

    prv = prev_arr[target]
    prev_arr[i] = prv
    next_arr[prv] = i

    alive[target] = False

# [Main]
N, M = map(int, input().split())
stations = list(map(int, input().split()))

tail = 0
for station in stations:
    tail = append_station(tail, station)

for _ in range(M):
    parts = input().split()
    cmd = parts[0]
    i = int(parts[1])

    if cmd == "BN":
        run_bn(i, int(parts[2]))
    elif cmd == "BP":
        run_bp(i, int(parts[2]))
    elif cmd == "CN":
        run_cn(i)
    elif cmd == "CP":
        run_cp(i)

print("\n".join(result))

# [Declar Class and Funs]
# 객체 => TIMEOUT
def sol_by_class():
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.prev = None
            self.next = None

    result = []
    class CircularLinkedList:
        global result

        def __init__(self):
            self.tail = None
            self.d_size = 0
            self.station_nums = [False] * (1000000 + 1)
            self.prev_arr = [None] * (1000000 + 1)
            self.next_arr = [None] * (1000000 + 1)

        def append_station(self, data):
            # 이미 설립된 역
            if self.station_nums[data]:
                return

            new_node = Node(data)
            if not self.d_size:
                new_node.prev = new_node
                new_node.next = new_node
        
                self.tail = new_node
                self.station_nums[data] = new_node

                self.d_size += 1
                return
            
            head = self.tail.next

            new_node.prev = self.tail
            new_node.next = head

            self.tail.next = new_node
            head.prev = new_node

            self.tail = new_node
            self.station_nums[data] = new_node

            self.d_size += 1

        def run_bn(self, station_num, new_station_num):
            # i + 1 출력
            # i - j - (i+1), j 삽입

            # 이미 설립된 역
            if self.station_nums[new_station_num]:
                return

            new_node = Node(new_station_num)
            if cur_node := self.station_nums[station_num]:
                result.append(str(cur_node.next.data))
                new_node.prev = cur_node
                new_node.next = cur_node.next

                cur_node.next.prev = new_node
                cur_node.next = new_node

                self.station_nums[new_station_num] = new_node
                self.d_size += 1
                

        def run_bp(self, station_num, new_station_num):
            # i - 1 출력
            # (i-1) - j - i, j 삽입

            # 이미 설립된 역
            if self.station_nums[new_station_num]:
                return
            
            new_node = Node(new_station_num)
            if cur_node := self.station_nums[station_num]:
                result.append(str(cur_node.prev.data))
                new_node.prev = cur_node.prev
                new_node.next = cur_node

                cur_node.prev.next = new_node
                cur_node.prev = new_node

                self.station_nums[new_station_num] = new_node
                self.d_size += 1

        def run_cp(self, station_num):
            # i - 1 폐쇄 후 출력
            if cur_node := self.station_nums[station_num]:
                del_station_num = cur_node.prev.data
                result.append(str(del_station_num))
                prev_node = cur_node.prev.prev
                next_node = cur_node

                prev_node.next = next_node
                next_node.prev = prev_node

                self.station_nums[del_station_num] = None
                self.d_size -= 1

        def run_cn(self, station_num):
            # i + 1 폐쇄 후 출력
            if cur_node := self.station_nums[station_num]:
                del_station_num = cur_node.next.data
                result.append(str(del_station_num))
                prev_node = cur_node
                next_node = cur_node.next.next

                prev_node.next = next_node
                next_node.prev = prev_node

                self.station_nums[del_station_num] = None
                self.d_size -= 1

    # [Main 풀이]
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    stations = list(map(int, input().split()))

    # 역 고유번호 저장, print 결과 저장 배열, 현재 역 저장
    station_list = CircularLinkedList()

    # O(N)
    for station in stations:
        station_list.append_station(station)

    # O(M)
    for _ in range(M):
        parts = input().split()
        type, i, j = parts[0], int(parts[1]), int(parts[2]) if len(parts) > 2 else None

        if type == "BN":
            station_list.run_bn(i, j)
        elif type == "BP":
            station_list.run_bp(i, j)
        elif station_list.d_size > 1:
            if type == "CP":
                station_list.run_cp(i)
            elif type == "CN":
                station_list.run_cn(i)

    # O(result)
    print("\n".join(result))

'''
조건
- BN: 현재가 i면, i+1 출력 -> i - j - (i+1) (j 삽입)
- BP: 현재가 i면, i-1 출력 -> (i-1) - j - i (j 삽입)
- CN: 현재가 i면, i+1 폐쇄 -> 출력
- CP: 현재가 i면, i-1 폐쇄 -> 출력

- CN, CP는 역이 2개 이상일 때만 들어옴
- 이미 설립된 역은 또 설립될 수 없음
- 폐쇄된 역은 다시 설립될 수 있음

0. 제한사항
    시간: 2초 (2천만번)
    메모리: 512 MB (대충 100만 ~ 500만 기준으로 생각하기)

1. Constraints
    입력:
        [0] 공사 전 역 개수 = N (1 ~ 500,000)
        [0] 공사 횟수 = M (1 ~ 1,500,000)
        [1] 역의 고유 번호 = 1 ~ 1,000,000
        [2~] 공사 정보
        * 원형, 시계방향으로 역 제공

2. Ideas
    핵심 연산: 임의 위치 조회 삽입, 삭제 
        - 원형 연결, 역과 역 사이의 insert, delete, 역 사이즈 체크, 역 중복체크(해시집합)
    호출 횟수: 500,000 + 1,500,000 = 2,000,000 (200만번) O(N)필요
    필요 복잡도: 삽입, 삭제 = O(1)

    의문점: 공사 정보마다 역을 조회해야하고 그럼 O(N)이 될텐데, 그게 M만큼 있으면 시간초과아닌가? N*M이니까.
        => '역은 고유하다' 그러면 조회를 O(1)로 바꿔야한다. O(1)인 것, 해시 혹은 인덱스 접근 배열

    1) 삽입, 삭제가 O(1)인 원형 Linked List 사용
        - tail Node로 관리
        - tail.next == head가 되기 때문에 하나로 끝과 시작을 관리하기 쉬움
    2) 조회가 O(1)인 해시 집합 or 인덱스 접근 배열 사용
        - 해시 집합은 상수 비용을 고려해야함
        - 접근 배열 최대가 1,000,000인데 메모리 512MB이니까 상수 비용이 더 적은 접근 배열 생성
        🔥 이 부분 판단 기준 팀원들이랑 이야기 나눠보면 좋을 듯

3. Complextity
    시간복잡도:
    공간복잡도:
'''