import time
import statistics

REPEATS = 100

def mean_microseconds(func):
    times = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1_000_000)
    return statistics.mean(times)

results = []

for size in [10, 1000, 1_000_000]:
    results.append(mean_microseconds(
        lambda s=size: list(range(s)).insert(0, -1)
    ))

for size in [10, 1000, 1_000_000]:
    results.append(mean_microseconds(
        lambda s=size: list(range(s)).pop(0)
    ))

for size in [10, 1000, 1_000_000]:
    results.append(mean_microseconds(
        lambda s=size: list(range(s)).append(-1)
    ))

for size in [10, 1000, 1_000_000]:
    results.append(mean_microseconds(
        lambda s=size: list(range(s)).pop()
    ))

for size in [10, 1000, 1_000_000]:
    lst = list(range(size))
    results.append(mean_microseconds(
        lambda l=lst: 0.123 in l
    ))

for size in [10, 1000, 1_000_000]:
    d = {i: i for i in range(size)}
    results.append(mean_microseconds(
        lambda dct=d: 0.123 in dct
    ))

for value in results:
    print(value)
