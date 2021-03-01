#include "test-linalg.h"
#include <nos/print.h>

TEST_CASE_TEMPLATE("pinv", T, float, double)
{
    linalg::mat<T,3,2> m = 
    {
        {1.3,0,0},
        {4,0,0}
    };

    nos::println(pinv(m));

    CHECK(fabs(determinant(mul(pinv(m), m)) - 1) < 1e-5);
}
