#pragma once

#include <cstddef>

template<typename T>
class IterationMethod {
protected:
  T current;

public:
  virtual void setInitialState(const T& init) = 0;

  virtual void makeStep() = 0;

  void makeSteps(size_t n) {
    while (n--)
      makeStep();
  }

  const T& getCurrent() const {
    return current;
  }
};