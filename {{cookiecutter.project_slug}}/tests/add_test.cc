#include "add.h"
#include "gtest/gtest.h"

TEST(ADD, AddTest) {
  EXPECT_EQ(my_add(1, 2), 3);
  EXPECT_EQ(my_add(-1, 1), 0);

}