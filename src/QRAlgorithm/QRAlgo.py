from utils import *
from GivensRotation import *


def fixAQ(A, Q, qr_dec):
    Qk, Rk = qr_dec(A)
    if type(Qk) == Matrix:
        A = Rk * Qk
        Q *= Qk
    else:
        A = Rk
        for (i, j, c, s) in Qk:
            givens_mul_right(A, i, j, c, s)
            givens_mul_right(Q, i, j, c, s)
    return A, Q


def QRAlgo(A, eps=global_eps, qr_dec=QR_Givens):
    A.square()
    A.symmetric()

    Q = Matrix.unit(A.width)

    while not A.circle_check(eps):
        A, Q = fixAQ(A, Q, qr_dec)

    eigens = [A[i][i] for i in range(A.width)]
    return eigens, Q
