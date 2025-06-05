#include <benchmark/benchmark.h>

#include "add.h"

static void BM_ADD(benchmark::State &state) {
  for (auto _ : state) {
    my_add(1, 2);
  }
}

BENCHMARK(BM_ADD)->Arg(10000);

BENCHMARK_MAIN();