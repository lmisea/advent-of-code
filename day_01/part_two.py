import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            calibration_sum = 0
            spelled_numbers = [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]

            for line in input_file:
                numbers = []
                for index, char in enumerate(line):
                    # If a character is a number, add it to the numbers list
                    if char.isnumeric():
                        numbers.append(char)
                    else:
                        # If a character is a letter, check if it is the start of a spelled number
                        for order, spelled_number in enumerate(spelled_numbers):
                            # If the character and the following characters match a spelled number
                            # add the spelled number value to the numbers list
                            if (
                                line[index : index + len(spelled_number)]
                                == spelled_number
                            ):
                                numbers.append(str(order + 1))
                                break

                if numbers:  # Skip the line if there a no numbers
                    calibration_value = int(numbers[0] + numbers[-1])
                    calibration_sum += calibration_value

            if print_output:
                print(f"Sum of all calibration values: {calibration_sum}")
                sys.exit(0)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
