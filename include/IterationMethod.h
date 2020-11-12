#pragma once

#include <cstddef>

namespace LinearAlgebra {

  template<typename T>
  class IterationMethod {
  protected:
    T current;

  public:
    virtual void setInitialState(const T &init) {
      current = init;
    }

    virtual void makeStep() = 0;

    void makeSteps(size_t n) {
      while (n--)
        makeStep();
    }

    const T &getCurrent() const {
      return current;
    }
  };

}