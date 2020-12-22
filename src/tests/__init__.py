from utils import *
from SIM import *
from GaussZeidel import *
from GivensRotation import *
from HHTransform import *
from QRAlgorithm import *
from Tridiagonal import *
from Graphs import *
import random

eps = 1e-14


def SIM_test(A, b):
    x = simple_iteration_method(A, b, eps)
    assert (x == A * x + b)
    print("SIM_test: OK")


def GZ_test(A, b):
    x = gauss_zeidel(A, b, eps)
    assert (A * x == b)
    print("GZ_test: OK")


def QR_dec_test(A, qr_dec):
    Q, R = qr_dec(A)
    if type(Q) != Matrix:
        tmp = Q
        Q = Matrix.unit(A.width)
        for (i, j, c, s) in tmp:
            givens_mul_right(Q, i, j, c, s)

    assert (Q * (Q.transpose()) == Matrix.unit(Q.width))

    for i in range(R.height):
        for j in range(i):
            assert (eq(R[i][j], 0))

    assert (Q * R == A)
    print(f"{qr_dec.__name__}_test: OK")


def SI_test(A):
    x = Matrix.random(A.width, 1)
    k, v = simple_iteration(A, x, eps)
    assert (A * v == k * v)
    print("SI_test: OK")


def QRAlgo_test(A, qr_dec=QR_Givens):
    evals, Q = QRAlgo(A, eps, qr_dec)

    for i in range(Q.width):
        evector = Matrix.vector([Q[j][i] for j in range(Q.height)])
        assert (A * evector == evals[i] * evector)
    print(f"QRAlgo_{qr_dec.__name__}_test: OK")


def Tridiagonalization_test(A):
    B, Q = tridiagonalization(A)
    B.tridiagonal()
    assert (Q.transpose() * A * Q == B)
    return B


def FastQRAlgo_test(A):
    evals, Q = FastQRAlgo(A, eps)

    for i in range(Q.width):
        evector = Matrix.vector([Q[j][i] for j in range(Q.height)])
        assert (A * evector == evals[i] * evector)
    print("FastQRAlgo_test: OK")


def gen_random_shuffle_matrix(n):
    p = [i for i in range(n)]
    random.shuffle(p)
    P = Matrix.zero(n, n)
    rP = Matrix.zero(n, n)
    for i in range(n):
        P[i][p[i]] = 1
        rP[p[i]][i] = 1
    assert (P * rP == Matrix.unit(n))
    return P, rP


def shuffle_matrix(A):
    P, rP = gen_random_shuffle_matrix(A.width)
    return P * A * rP


def Isomorphism_test(A, B, exp):
    assert (isomorphism(A, A) == 1)
    assert (isomorphism(B, B) == 1)
    assert (isomorphism(A, B) == exp)
    C = shuffle_matrix(A)
    assert (isomorphism(A, C) == 1)
    C = shuffle_matrix(B)
    assert (isomorphism(B, C) == 1)

    print("Isomorphism_test: OK")


def Expanders_test():
    A = build_nxn(2)
    assert (eq(count_alpha(A), 0.5))
    A = build_p_inf(2)
    assert (eq(count_alpha(A), 0.57735027))
    print("Expanders_test: OK")


def run_all_tests():
    A = Matrix([
        [0.4, 0],
        [0.2, 0.01]
    ])
    E = Matrix.unit(2)
    b = Matrix.vector([0.8, 0.43])

    SIM_test(E - A, b)
    GZ_test(A, b)

    A = Matrix([
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 0]
    ])
    QR_dec_test(A, QR_Givens)
    QR_dec_test(A, QR_Householder)

    SI_test(A)

    A = Matrix([
        [4, 1, 1, 0, 0],
        [1, -1.1, 1, 2, -1],
        [1, 1, -3, 0.02, 0.02],
        [0, 2, 0.02, 0, 5],
        [0, -1, 0.02, 5, -1]
    ])

    QRAlgo_test(A)
    B = Tridiagonalization_test(A)
    QR_dec_test(B, QR_Tridiagonal)
    QRAlgo_test(B, QR_Tridiagonal)
    FastQRAlgo_test(B)

    C = Matrix([
        [1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ])
    D = Matrix([
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0]
    ])

    Isomorphism_test(C, D, 0)

    Expanders_test()

    print("-------")
    print("All tests: OK")
