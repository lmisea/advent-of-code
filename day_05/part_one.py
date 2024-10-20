import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            # Each block of data is separated by two newlines
            # The first block contains the seeds
            # *blocks stores the remaining blocks on the blocks var
            seeds, *blocks = input_file.read().split("\n\n")

            # Let's parse seeds into a list of integers
            seeds = list(map(int, seeds.split(":")[1].split()))

            for block in blocks:
                conversions = []
                # We get rid of the first line of the block (the block's identifier)
                # [1:] is a slice that returns all elements of a list except the first one
                for line in block.splitlines()[1:]:
                    # We split the line by spaces and convert the elements to integers
                    conversions.append(list(map(int, line.split())))

                # We convert the original seeds into their final locations by applying the conversions
                converted = []
                for item in seeds:
                    for destination, source, length in conversions:
                        # Check if the item is within the range of the source
                        if source <= item < source + length:
                            converted.append(item - source + destination)
                            break
                    # The else block is executed if the for loop completes without breaking
                    else:
                        converted.append(item)
                seeds = converted

            # We find the minimum item in the list for the minimum location
            min_loc = min(seeds)

            if print_output:
                print(f"The minimum location is: {min_loc}")

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
