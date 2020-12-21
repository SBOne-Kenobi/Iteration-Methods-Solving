# (I - 2v * v^T) * A
def householder_mul(A, v):
    return A - (2 * v) * (v.transpose() * A)


# A * (I - 2v * v^T)
def householder_mul_right(A, v):
    return A - (A * (2 * v)) * v.transpose()
