import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            # Each block of data is separated by two newlines
            # The first block contains the seeds ranges but not parsed yet
            # *blocks stores the remaining blocks on the blocks var
            inputs, *blocks = input_file.read().split("\n\n")

            # Let's parse the seeds ranges into a list of integers
            ranges = list(map(int, inputs.split(":")[1].split()))

            # Let's calculate the actual ranges
            seeds = []
            for i in range(0, len(ranges), 2):
                seeds.append((ranges[i], ranges[i] + ranges[i + 1]))

            for block in blocks:
                conversions = []
                # We get rid of the first line of the block (the block's identifier)
                # [1:] is a slice that returns all elements of a list except the first one
                for line in block.splitlines()[1:]:
                    # We split the line by spaces and convert the elements to integers
                    conversions.append(list(map(int, line.split())))

                # We convert the range of the seeds into their final locations by applying the conversions
                converted = []
                while seeds:
                    start, end = seeds.pop()  # We pop the last item from the list
                    for destination, source, length in conversions:
                        # Check if any range of the conversions overlaps with the current range (start, end)
                        overlap_start = max(start, source)
                        overlap_end = min(end, source + length)
                        # Convert the overlapping range
                        if overlap_start < overlap_end:
                            converted.append(
                                (
                                    overlap_start - source + destination,
                                    overlap_end - source + destination,
                                )
                            )
                            # If the overlapping range cuts the current range, we add the remaining ranges to the seeds
                            if overlap_start > start:
                                seeds.append((start, overlap_start))
                            if overlap_end < end:
                                seeds.append((overlap_end, end))
                            break
                    # The else block is executed if the for loop completes without breaking
                    else:
                        converted.append((start, end))

                seeds = converted

            # We find the minimum range of resulting locations ranges and get the first location
            # in that range to get the minimum location
            min_loc = min(seeds)[0]

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
