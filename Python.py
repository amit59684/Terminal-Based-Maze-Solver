from random import randint

class Node:
    def __init__(self, value=None, next_element=None):
        self.val = value
        self.next = next_element

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            returned = self.head.val
            self.head = self.head.next
            self.length -= 1
            return returned

    def fill(self):
        return bool(self.length)

    def top(self):
        return self.head.val

M = [] 
path = []


def Genarate_new_M(R, C, MS, MF):
    global M

    M = [[0 for i in range(C)] for i in range(R)]
    seen = [[False for i in range(C)] for i in range(R)]
    pre = [[(-1, -1) for i in range(C)] for i in range(R)]

    S = Stack()
    S.insert(MS)

    while S.fill():
        x, y = S.pop()
        seen[x][y] = True

        if (x + 1 < R) and M[x + 1][y] == 1 and pre[x][y] != (x + 1, y):
            continue
        if (0 < x) and M[x-1][y] == 1 and pre[x][y] != (x-1, y):
            continue
        if (y + 1 < C) and M[x][y + 1] == 1 and pre[x][y] != (x, y + 1):
            continue
        if (y > 0) and M[x][y-1] == 1 and pre[x][y] != (x, y-1):
            continue

        M[x][y] = 1
        ts = []

        if (x + 1 < R) and not seen[x + 1][y]:
            seen[x + 1][y] = True
            ts.append((x + 1, y))
            pre[x + 1][y] = (x, y)

        if (0 < x) and not seen[x-1][y]:
            seen[x-1][y] = True
            ts.append((x-1, y))
            pre[x-1][y] = (x, y)

        if (y + 1 < C) and not seen[x][y + 1]:
            seen[x][y + 1] = True
            ts.append((x, y + 1))
            pre[x][y + 1] = (x, y)

        if (y > 0) and not seen[x][y-1]:
            seen[x][y-1] = True
            ts.append((x, y-1))
            pre[x][y-1] = (x, y)

        MF_flag = False
        while ts:
            neighbour = ts.pop(randint(0, len(ts) - 1))
            if neighbour == MF:
                MF_flag = True
            else:
                S.insert(neighbour)

        if MF_flag:
            S.insert(MF)

    x0, y0 = MS
    xf, yf = MF
    M[x0][y0] = 2
    M[xf][yf] = 3
    return M