#include "Matrix.h"
#include <iostream>

int main() {

  LinearAlgebra::Matrix<int> A, B;
  std::freopen("input.txt", "r", stdin);
  std::cin >> A >> B;
  std::cout << A * B;

  return 0;
}