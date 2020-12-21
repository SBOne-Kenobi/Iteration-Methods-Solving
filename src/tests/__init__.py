from utils import *
from SIM import *
from GaussZeidel import *
from GivensRotation import *
from HHTransform import *

eps = 1e-14


def SIM_test(A, b):
    x = simple_iteration(A, b, eps)
    assert (x == A * x + b)


def GZ_test(A, b):
    x = gauss_zeidel(A, b, eps)
    assert (A * x == b)


def QR_test(A, qr_alg):
    Q, R = qr_alg(A)
    assert (Q * (Q.transpose()) == Matrix.unit(Q.width))

    for i in range(R.height):
        for j in range(i):
            assert (eq(R[i][j], 0))

    assert (Q * R == A)


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
    QR_test(A, QR_Givens)
    QR_test(A, QR_Householder)
