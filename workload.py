import time
import numpy as np
import random

def cpu_intensive_task(duration):
    print("Starting CPU-intensive task...")
    end_time = time.time() + duration
    while time.time() < end_time:
        # Perform some CPU-intensive calculations
        [x**2 for x in range(10000)]
    print("CPU-intensive task completed.")

def memory_allocation_task(size_mb, duration):
    print("Starting memory allocation task...")
    end_time = time.time() + duration
    arrays = []
    while time.time() < end_time:
        # Allocate large arrays to simulate memory usage
        array = np.zeros((size_mb * 1024 * 1024 // 8,), dtype='float64')
        arrays.append(array)
        time.sleep(0.1)  # Adjust the sleep time to control allocation rate
    print("Memory allocation task completed.")

def memory_access_pattern_task(size_mb, duration, pattern='sequential'):
    print(f"Starting memory access pattern task ({pattern})...")
    array = np.zeros((size_mb * 1024 * 1024 // 8,), dtype='float64')
    end_time = time.time() + duration
    if pattern == 'sequential':
        while time.time() < end_time:
            for i in range(len(array)):
                array[i] = random.random()
    elif pattern == 'random':
        while time.time() < end_time:
            for _ in range(len(array)):
                array[random.randint(0, len(array) - 1)] = random.random()
    print(f"Memory access pattern task ({pattern}) completed.")

def matrix_computation():
    size = 10000
    matrix_a = np.random.rand(size, size)
    matrix_b = np.random.rand(size, size)
    
    # Perform a matrix multiplication
    result = np.dot(matrix_a, matrix_b)
    
    return result

def sequential_access():
    # Access data sequentially to increase cache hits
    array_size = 10**6
    data = np.zeros(array_size)
    
    for i in range(array_size):
        data[i] += 1

def random_access():
    # Access data randomly, which may lead to more cache misses
    array_size = 10**6
    data = np.zeros(array_size)
    
    for _ in range(array_size):
        i = np.random.randint(0, array_size)
        data[i] += 1

def main():
    cpu_duration = 150      # Duration of CPU-intensive task in seconds
    mem_size_mb = 100      # Size of memory to allocate/access in MB
    mem_duration = 150     # Duration of memory tasks in seconds

    # Perform CPU-intensive task
    cpu_intensive_task(cpu_duration)

    # Perform memory allocation task
    memory_allocation_task(mem_size_mb, mem_duration)

    # Perform memory access pattern task (sequential)
    memory_access_pattern_task(mem_size_mb, mem_duration, pattern='sequential')

    # Perform memory access pattern task (random)
    memory_access_pattern_task(mem_size_mb, mem_duration, pattern='random')
    print("Starting heavy computation...")
    matrix_computation()
    print("Heavy computation done.")
    
    # Sequential access to data
    print("Starting sequential data access...")
    sequential_access()
    print("Sequential access done.")
    
    # Random access to data
    print("Starting random data access...")
    random_access()
    print("Random access done.")

if __name__ == "__main__":
    main()
