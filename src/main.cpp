#include "Matrix.h"
#include "SimpleIterationMethod.h"

#include <iostream>

using namespace LinearAlgebra;

int main() {

  freopen("input.txt", "r", stdin);

  LinearAlgebra::Matrix<double> A, b;
  std::cin >> A >> b;
  A = SimpleIterationMethod<double>::getStepMatrixFromEquationMatrix(A);
  SimpleIterationMethod method(A, b);
  method.setInitialState(Matrix<double>(3, 1, 1));
  method.makeSteps(100);
  std::cout << method.getCurrent() << "\n";

  return 0;
}