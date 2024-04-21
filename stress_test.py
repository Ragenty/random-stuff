import multiprocessing
import os
import time
import platform
import re

def cpu_bound_task(difficulty):
    """Simulates a CPU-bound task."""
    result = 0
    for _ in range(10**difficulty):
        result += 1
    return result

def stress_test(num_processes, difficulty):
    """Runs a CPU stress test by spawning multiple processes."""
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_bound_task, args=(difficulty,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

def detect_cpu_speed():
    """Detects the CPU speed by parsing the processor information."""
    # Get processor information from platform module
    info = platform.processor()
    
    # Extract CPU speed from processor information using regular expressions
    match = re.search(r'\d+', info)
    if match:
        cpu_speed = int(match.group())
        print(f"CPU speed: {cpu_speed / 1000:.2f} GHz")
    else:
        print("Unable to detect CPU speed.")

if __name__ == "__main__":
    # Detect and print CPU speed
    detect_cpu_speed()
    
    # Determine the number of CPU cores and threads
    num_cores = os.cpu_count()
    num_threads = num_cores * 2
    print(f"Detected {num_cores} cores and {num_threads} threads.")
    
    # User input for difficulty level
    difficulty = int(input("Enter the difficulty level (recommended between 7 and 9): "))
    if difficulty < 7:
        print("Warning: Difficulty level below recommended range.")
    elif difficulty > 9:
        print("Warning: Difficulty level above recommended range.")
    
    # Start CPU stress test
    print("Starting CPU stress test...")
    start_time = time.time()
    stress_test(num_threads, difficulty)
    end_time = time.time()
    
    # Calculate and print the duration of the stress test
    duration = end_time - start_time
    print(f"CPU stress test completed in {duration:.2f} seconds.")
