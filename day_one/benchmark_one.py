import timeit

from part_one import main

if __name__ == "__main__":
    # Measure the average execution time using timeit
    execution_times = timeit.repeat(
        "main(print_output=False)", globals=globals(), repeat=10, number=1
    )
    average_time = sum(execution_times) / len(execution_times)

    print(f"Average execution time over 10 runs: {average_time:.6f} seconds")
