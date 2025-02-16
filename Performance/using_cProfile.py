import cProfile

# Function to test
def calculate_sum(n):
    return sum(range(n))

# Run the profiler
cProfile.run('calculate_sum(1000000)')