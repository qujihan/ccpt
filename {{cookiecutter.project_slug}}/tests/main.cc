#include "add.h"
#include "gtest/gtest.h"

TEST(BasicTest, AddTest) {
  auto ans = my_add(1, 2);
  EXPECT_EQ(ans, 3);
}

int main(int argc, char **argv) {  // NOLINT
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}