import copy


def print_nice(U):
    print
    for i in range(N):
        for j in range(M):
            if U[i][j]>=0:
                print '% 7.3f ' % U[i][j],
            else:
                print '% 7.3f ' % U[i][j],               
        print
    print


# problem specific
# -----------------------------
"""

    0
3       1
    2

"""

board = [
    ['.','.','.','g'],
    ['.','-','.','b'],
    ['.','.','.','.'],
]


h = {}
h[0] = (-1, 0)
h[1] = (0, 1)
h[2] = (1, 0)
h[3] = (0, -1)
X = 1
gamma = 1.0
delta = 1.0 * X / 20.0
delta = 0.000001

N = 3
M = 4
NA = 4
NS = 4
# -----------------------------



P = [[[[0.0 for l in range(NS)] for k in range(NA)] for j in range(M)] for i in range(N)]
S = [[[[(0,0) for l in range(NS)] for k in range(NA)] for j in range(M)] for i in range(N)]
R = [[[[0.0 for l in range(NS)] for k in range(NA)] for j in range(M)] for i in range(N)]


U = [[0 for j in range(M)] for i in range(N)]
# UT = [[0 for j in range(M)] for i in range(N)]
U[0][3] = X
U[1][3] = -X


# problem specific
# ----------------------------
for i in range(N):
    for j in range(M):
        for k in range(NA):

            for l in range(NS):

                if k==l :
                    P[i][j][k][l] = 0.8
                elif (k+1)%NA == l  or (k-1+NA)%NA==l :
                    P[i][j][k][l] = 0.1
                else :
                    P[i][j][k][l] = 0.0

                r, c = h[l]
                nr = i+r
                nc = j+c

                if nr >= N or nr < 0 or nc >= M or nc < 0 or board[nr][nc] == '-':
                    S[i][j][k][l] = (i, j)
                else:
                    S[i][j][k][l] = (nr, nc)

                r, c = S[i][j][k][l]

                if board[r][c] == '.':
                    R[i][j][k][l] = -1.0 * X / 25.0
                elif board[r][c] == 'g':
                    R[i][j][k][l] = -1.0 * X / 25.0
                    #R[i][j][k][l] = X
                elif board[r][c] == 'b':
                    R[i][j][k][l] = -1.0 * X / 25.0
                    #R[i][j][k][l] = -X
                else:
                    R[i][j][k][l] = -1.0 * X / 25.0
                R[i][j][k][l] = -0.002
# ----------------------------

for i in range(N):
    for j in range(M):
        print P[i][j]


count = 0
change = X

while count < 1000:

    print "Iteration :",count
    print_nice(U)

    UT = copy.deepcopy(U)
    
    change = 0
    for i in range(N):
        for j in range(M):

            if board[i][j] == '-' or board[i][j] == 'g' or board[i][j] == 'b':
                continue

            max_value = -1000000
            for k in range(NA):
                value = 0
                for l in range(NS):
                    r, c = S[i][j][k][l]
                    value += P[i][j][k][l] * (UT[r][c] * gamma + R[i][j][k][l])

                max_value = max(max_value, value)

            U[i][j] = max_value
            change = max(change, abs(U[i][j] - UT[i][j]))
    
    count += 1
    del UT

print "Iteration :",count
print_nice(U)


policy = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):

        if board[i][j] != '.':
            continue

        po = 0
        max_value = -10000

        for k in range(NA):
            value = 0

            for l in range(NS):
                r, c = S[i][j][k][l]
                value += P[i][j][k][l] * (U[r][c] * gamma + R[i][j][k][l])
            
            if value > max_value:
                max_value = value
                po = k
        
        policy[i][j] = po

print
print "Policy"
print
print_nice(policy)
