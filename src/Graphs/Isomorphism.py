from QRAlgorithm import *
from Tridiagonal import *
from utils import *


def checkDegrees(A, B):
    a = sorted([(sum(A[i]), A[i][i]) for i in range(A.width)])
    b = sorted([(sum(B[i]), B[i][i]) for i in range(B.width)])
    return a == b


def get_eigens(A):
    eigens, _ = FastQRAlgo(A)
    return sorted(eigens)


def checkEigens(A, B):
    a, b = get_eigens(A), get_eigens(B)
    for i in range(len(a)):
        if not eq(a[i], b[i]):
            return False
    return True


def dfs(v, A, used):
    used[v] = True
    cnt_v = 1
    cnt_e = sum(A[v])
    for u in range(A.width):
        if A[v][u] == 1 and not used[u]:
            cv, ce = dfs(u, A, used)
            cnt_e += ce
            cnt_v += cv
    return cnt_v, cnt_e


def get_comp(A):
    n = A.width
    used = [False] * n
    cnt = []
    for i in range(n):
        if not used[i]:
            cnt.append(dfs(i, A, used))
    return sorted(cnt)


def check_comp(A, B):
    return get_comp(A) == get_comp(B)


def isomorphism(A, B):
    A.square()
    A.symmetric()
    B.square()
    B.symmetric()

    if A == B:
        return 1

    if A.width != B.width:
        return 0

    if not checkDegrees(A, B):
        return 0

    AT, _ = tridiagonalization(A)
    BT, _ = tridiagonalization(B)

    if not checkEigens(AT, BT):
        return 0

    if not check_comp(A, B):
        return 0

    return 1
