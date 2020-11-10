#pragma once

#include <type_traits>

namespace LinearAlgebra {

  template<typename T,
          std::enable_if_t<std::is_arithmetic<T>::value, bool> = true>
  class ArithmeticRestriction {
  };

}