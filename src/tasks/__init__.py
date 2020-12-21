from utils import *
from SIM import *
from GaussZeidel import *
from GivensRotation import *
from HHTransform import *


def print_ans(x):
    print("Ответ:")
    for name, val in x:
        print(f"{name} = \n{val}")


# |x - Ax - b| < eps
def task_1():
    A = input_matrix()
    b = input_vector()
    eps = input_accuracy()
    x = simple_iteration(A, b, eps)
    print_ans([
        ("x", x)
    ])


# |Ax - b| < eps
def task_2():
    A = input_matrix()
    b = input_vector()
    eps = input_accuracy()
    x = gauss_zeidel(A, b, eps)
    print_ans([
        ("x", x)
    ])


def task_3():
    A = input_matrix()
    print("Введите 2 числа через пробел - 2 индекса: ")
    i, j = map(int, input().split())
    print("Введите 2 числа через пробел - c, s (c^2 + s^2 = 1)")
    c, s = map(float, input().split())
    givens_mul(A, i, j, c, s)
    print_ans([
        (f"G({i}, {j}, {c}, {s}) A", A)
    ])


def task_4():
    A = input_matrix()
    Q, R = QR_Givens(A)
    print_ans([
        ("Q", Q),
        ("R", R)
    ])


def task_5():
    A = input_matrix()
    v = input_vector()
    HA = householder_mul(A, v)
    print_ans([
        ("Hv * A", HA)
    ])


def task_6():
    A = input_matrix()
    Q, R = QR_Householder(A)
    print_ans([
        ("Q", Q),
        ("R", R)
    ])


all_tasks = [task_1, task_2, task_3, task_4, task_5, task_6]


def run_all_tasks():
    for i in range(len(all_tasks)):
        print(f"Задача \n{i + 1}:")
        all_tasks[i]()
        print("----------------\n")
