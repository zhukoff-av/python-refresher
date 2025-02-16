import timeit


# The timeit module is designed for small code snippets and provides more accurate timing by running the code multiple times.

# Function to test
def calculate_sum(n):
    return sum(range(n))


# Performance test using timeit
def test_performance():
    # timeit automatically runs the function multiple times for accuracy
    elapsed_time = timeit.timeit(lambda: calculate_sum(1000000), number=100)
    print(f"Elapsed time for 100 runs: {elapsed_time:.6f} seconds")
    print(f"Average time per run: {elapsed_time / 100:.6f} seconds")


# Run the performance test
test_performance()
