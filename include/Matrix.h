#pragma once

#include <vector>
#include <algorithm>
#include "ArithmeticRestriction.h"

namespace LinearAlgebra {

  class MismatchMatrixSize : public std::logic_error {
  public:
    MismatchMatrixSize() : logic_error("Mismatched matrix size") {}
  };

  template<typename T>
  class Matrix : ArithmeticRestriction<T> {
  private:
    T *_data;
    size_t _cols;
    size_t _rows;

    bool check_size(const Matrix &other) const;

  public:
    Matrix(size_t rows, size_t cols, const T &value = T());

    Matrix(const Matrix &other);

    template<typename U>
    friend void swap(Matrix<U>& a, Matrix<U>& b);

    Matrix& operator=(const Matrix& other);

    [[nodiscard]] size_t rows() const;

    [[nodiscard]] size_t cols() const;

    T *operator[](size_t row);

    const T *operator[](size_t row) const;

    Matrix &operator+=(const Matrix &other);

    Matrix operator+(const Matrix &other) const;

    Matrix operator*(const Matrix &other) const;

    Matrix& operator*=(const Matrix &other);
  };

}