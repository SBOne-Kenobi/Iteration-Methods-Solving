from utils.matrix import *


def input_matrix():
    print("Введите размер матрицы - два числа через пробел: ")
    n, m = map(int, input().split())

    print("Введите матрицу (построчно): ")
    result = [0] * n
    for i in range(n):
        result[i] = list(map(float, input().split()))

    return Matrix(result)


def input_vector():
    print("Введите размер вектора: ")
    n = int(input())

    print("Введите вектор (по одному числу в строке): ")
    result = [0] * n
    for i in range(n):
        result[i] = float(input())

    return Matrix.vector(result)


def input_accuracy():
    print("Введите точность вычислений: ")
    accuracy = float(input())
    return accuracy
