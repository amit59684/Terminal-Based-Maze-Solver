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
P = []


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



def Show_M(M, P):
    S = {0: "*", 1: "_", 2: "1", 3: "2", -1: "0"}  
    M_copy = [row[:] for row in M]
    for x, y in P:
        M_copy[x][y] = -1
    for row in M_copy:
        print(" ".join(S[cell] for cell in row))


def dfs(Vis, Cord):
    global M, P
    
    if (not (Cord[0]>=0 and Cord[0]<len(M) and Cord[1]>=0 and Cord[1]<len(M))) or M[Cord[0]][Cord[1]]==0:
        return False
    
    if Cord[0]==len(M)-1 and Cord[1]==len(M)-1:
        return True

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    for dir in dirs:
        newC = (Cord[0]+dir[0], Cord[1]+dir[1])
        if (not (newC[0]>=0 and newC[0]<len(M) and newC[1]>=0 and newC[1]<len(M))):
            continue
        if (not Vis[newC[0]][newC[1]]):
            Vis[newC[0]][newC[1]] = True
            flag = dfs(Vis, newC)
            if flag:
                P.append(newC)
                return True
            else:
                Vis[newC[0]][newC[1]] = False
                
    return False

def Find_P():
    global M
    vis = [[False for i in range(len(M))] for i in range(len(M))]
    
    dfs(vis, (0,0))