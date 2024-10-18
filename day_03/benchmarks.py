import timeit
from part_one import main as part_one  # noqa: F401

if __name__ == "__main__":
    # Benchmark part_one
    execution_times = timeit.repeat(
        "part_one(print_output=False)", globals=globals(), repeat=50, number=1
    )
    average_time = sum(execution_times) / len(execution_times)

    print(f"Average execution time over 50 runs: {average_time:.6f} seconds")
