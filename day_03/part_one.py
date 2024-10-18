import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as grid_file:
            # Read the file into a list of lists (grid)
            grid = [list(line.strip()) for line in grid_file]
            coordinates = set()

            # We search for the symbols in the grid
            for y, row in enumerate(grid):
                for x, char in enumerate(row):
                    if char.isdigit() or char == ".":
                        continue
                    # If we find a symbol, we look for adjacent numbers
                    for cur_y in [y - 1, y, y + 1]:
                        for cur_x in [x - 1, x, x + 1]:
                            # Skip everything that is not a digit
                            if (
                                cur_y < 0
                                or cur_y >= len(grid)
                                or cur_x < 0
                                or cur_x >= len(grid[cur_y])
                                or not grid[cur_y][cur_x].isdigit()
                            ):
                                continue
                            # Once we find a digit, we move to the left until we can't anymore
                            while cur_x > 0 and grid[cur_y][cur_x - 1].isdigit():
                                cur_x -= 1
                            # We found the coordinates of the first digit of a part number
                            coordinates.add((cur_y, cur_x))

            # We obtain the part numbers
            part_numbers = []
            for y, x in coordinates:
                part_number = ""
                # We move to the right until we can't anymore
                while x < len(grid[y]) and grid[y][x].isdigit():
                    part_number += grid[y][x]
                    x += 1
                part_numbers.append(int(part_number))

            # Finally, we calculate the sum of the part numbers
            sum_part_numbers = sum(part_numbers)

            if print_output:
                print(f"Sum of the part numbers: {sum_part_numbers}")

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
