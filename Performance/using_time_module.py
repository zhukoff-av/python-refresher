import time


# Here’s an example using the time module to measure the execution time of a function

# Function to test
def calculate_sum(n):
    return sum(range(n))


# Performance test
def test_performance():
    start_time = time.time()  # Start time
    result = calculate_sum(1000000)  # Call the function
    end_time = time.time()  # End time

    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


# Run the performance test
test_performance()
