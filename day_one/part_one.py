import sys


def main(print_output: bool):
    try:
        with open("input_one.txt") as input_file:
            calibration_sum = 0

            for line in input_file:
                numbers = [char for char in line if char.isnumeric()]
                if numbers:  # Skip the line if there a no numbers
                    calibration_value = int(numbers[0] + numbers[-1])
                    calibration_sum += calibration_value

            if print_output:
                print(f"Sum of all calibration values: {calibration_sum}")
                sys.exit(0)

    except FileNotFoundError:
        print("The file input_one.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main(print_output=True)
