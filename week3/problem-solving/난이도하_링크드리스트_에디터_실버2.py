# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline

# 메모리 95,492 KB, 시간 804 ms
def solv_linked_list():
    # 개선된 풀이, cursor는 포인터, head는 dummy Node로 관리
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.prev = None
            self.next = None

    class Editor:
        def __init__(self):
            self.cursor = None
            self.head = Node()

            self.cursor = self.head

        def move_left_cursor(self):
            if self.cursor == self.head:
                return
            
            self.cursor = self.cursor.prev

        def move_right_cursor(self):
            if not self.cursor.next:
                return
            
            self.cursor = self.cursor.next

        def del_left_char(self):
            if self.cursor == self.head:
                return
            
            del_node = self.cursor
            prev_node = del_node.prev
            
            prev_node.next = del_node.next
            if del_node.next:
                del_node.next.prev = prev_node

            self.cursor = prev_node


        def append(self, data):
            new_node = Node(data)
            
            new_node.prev = self.cursor
            new_node.next = self.cursor.next

            if self.cursor.next:
                self.cursor.next.prev = new_node
            self.cursor.next = new_node

            self.cursor = new_node

        
        def print_list(self):
            values = []

            cur = self.head.next
            while cur:
                values.append(cur.data)
                cur = cur.next
            
            return values

    # 문제풀이
    L = input().strip()
    M = int(input())

    editor = Editor()

    # O(L) = O(100,000)
    for c in L:
        editor.append(c)

    # O(M) = O(500,000)
    for _ in range(M):
        parts = input().split()
        command, char = parts[0].strip(), parts[1].strip() if len(parts) > 1 else None
        
        if command == 'L':
            editor.move_left_cursor()
        elif command == 'D':
            editor.move_right_cursor()
        elif command == 'B':
            editor.del_left_char()
        else:
            editor.append(char)    

    # O(X) = O(600,000)
    print("".join(editor.print_list()))

# 메모리 42,832 KB, 시간 308 ms
def solv_two_stack():
    left_cursor = list(input().strip())
    right_cursor = []
    M = int(input())

    for _ in range(M):
        parts = input().split()
        command, char = parts[0].strip(), parts[1] if len(parts) > 1 else None

        if command == 'L':
            if left_cursor:
                right_cursor.append(left_cursor.pop())
        elif command == 'D':
            if right_cursor:
                left_cursor.append(right_cursor.pop())
        elif command == 'B':
            if left_cursor:
                left_cursor.pop()
        else:
            left_cursor.append(char)

    print("".join(left_cursor + right_cursor[::-1]))

solv_two_stack()


'''
조건
- 편집기는 영어 소문자만 기록 가능
- 최대 600,000 글자
- 명령어
    L: 커서 왼쪽 한 칸 (맨 앞이면 x)
    D: 커서 오른쪽 한 칸 (맨 뒤면 x)
    B: 커서 왼쪽 문자 삭제 (맨 앞이면 x)
    P $: $라는 문자를 커서 왼쪽에 추가함

0. 제한사항
    -> 시간 / 0.3초: 300만번
    -> 메모리 / 512 MB
    -> 출력: 편집기 문자열 최대 600,000

1. Constraints
    -> L: 편집기에 입력되어 있는 문자열
    -> N: 문자열의 길이 < 100,000
    -> M: 입력할 명령어의 개수 1 ~ 500,000

    -> 최대 시간 복잡도: O(L+M)
    -> 최대 공간 복잡도: O(L+M)

2. Ideas
    핵심 연산: 임의 위치 삽입/삭제
    호출 횟수: 최대 500,000번
    필요 복잡도: O(1) per operation

    1) 동적 List로 처리하기
        -> cursor(index) 인덱스를 정할때 왼쪽 오른쪽 삽입 기준을 정해야함.
        insert할때마다 O(N) -> 최악의 경우 O(100,000 * 500,000) = 50,000,000,000 (500억)

    2) Linked list
        -> cursor 포인터를 추가한다.
        -> head 더미 노드를 추가한다.
        -> 삽입, 삭제는 O(1), 근데 조회할때는 O(N) 최대 100,000 + 600,000 = 700,000
        -> 객체 하나당 오버헤드가 큼

    3) two stack
        -> 커서 기준으로 왼쪽 문자열을 담을 스택1, 오른쪽 문자열을 담을 스택2로 관리하기
        -> 삽입, 삭제는 O(1), 조회 시 O(N) 2랑 비슷 근데 linked list는 객체로 관리해야하니까 two stack이 더 효율적
'''





'''
# 첫 풀이, 복잡
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Editor:
    def __init__(self):
        self.cursor = Node(None)
        self.head = None

    def move_left_cursor(self):
        # 커서가 맨 앞이면 무시
        if not self.cursor.prev:
            return
        
        prev_node = self.cursor.prev
        self.cursor.prev = prev_node.prev
        self.cursor.next = prev_node

        if not self.cursor.prev:
            self.head = prev_node

    def move_right_cursor(self):
        # 커서가 맨 뒤면 무시
        if not self.cursor.next:
            return
        
        next_node = self.cursor.next
        self.cursor.prev = next_node
        self.cursor.next = next_node.next

    def del_left_char(self):
        # 커서가 맨 앞이면 무시
        if not self.cursor.prev:
            return            
        
        del_node = self.cursor.prev
        prev_node = del_node.prev
        next_node = self.cursor.next

        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif prev_node:
            prev_node.next = None
        elif next_node:
            next_node.prev = None

        self.cursor.prev = prev_node
        self.cursor.next = next_node

        if not self.cursor.prev:
            self.head = next_node


    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.cursor.prev = new_node
            return
        
        if not self.cursor.prev:
            next_node = self.head
            
            self.head = new_node
            self.cursor.prev = new_node
            self.cursor.next = next_node

            new_node.next = self.cursor.next
        else:
            prev_node = self.cursor.prev
            next_node = self.cursor.next

            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = next_node
            
            self.cursor.prev = new_node
            self.cursor.next = new_node.next

    def print_list(self):
        values = []
        
        current_node = self.head
        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return values
'''