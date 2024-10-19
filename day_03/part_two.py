import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as grid_file:
            # Read the file into a list of lists (grid)
            grid = [list(line.strip()) for line in grid_file]
            sum_gear_ratios = 0

            # We search for the gears in the grid (* with two adjacent part numbers)
            for y, row in enumerate(grid):
                for x, char in enumerate(row):
                    if char != "*":
                        continue
                    # If we find a '*', we look for two adjacent part numbers
                    adjacent_part_numbers = set()

                    # If we a find a '*', we check if it has two adjacent part numbers
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
                            adjacent_part_numbers.add((cur_y, cur_x))
                            # If we find more than two adjacent part numbers, it's not a gear
                            if len(adjacent_part_numbers) > 2:
                                break

                    if len(adjacent_part_numbers) != 2:
                        continue

                    # We obtain the two adjacent part numbers
                    part_numbers = []
                    for cur_y, cur_x in adjacent_part_numbers:
                        part_number = ""
                        # We move to the right until we can't anymore
                        while cur_x < len(grid[cur_y]) and grid[cur_y][cur_x].isdigit():
                            part_number += grid[cur_y][cur_x]
                            cur_x += 1
                        part_numbers.append(int(part_number))

                    # We add the gear ratio to the sum
                    sum_gear_ratios += part_numbers[0] * part_numbers[1]

            if print_output:
                print(f"Sum of the gear ratios: {sum_gear_ratios}")

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
