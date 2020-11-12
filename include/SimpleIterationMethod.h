#pragma once

#include "IterationMethod.h"
#include "Matrix.h"

namespace LinearAlgebra {

  template<typename T>
  class SimpleIterationMethod : public IterationMethod<Matrix<T>> {
  private:
    // x_{n+1} = stepMatrix * x_n + shiftMatrix
    Matrix<T> stepMatrix;
    Matrix<T> shiftMatrix;

  public:
    SimpleIterationMethod(const Matrix<T> &stepMatrix, const Matrix<T> &shiftMatrix) : stepMatrix(stepMatrix),
                                                                                       shiftMatrix(shiftMatrix) {}

    void makeStep() override {
      this->current = stepMatrix * this->current + shiftMatrix;
    }

    static Matrix<T> getStepMatrixFromEquationMatrix(const Matrix<T> &em) {
      return Matrix(std::vector<T>(em.rows(), 1)) - em;
    }
  };

}