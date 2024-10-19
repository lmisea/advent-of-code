import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            points = 0

            for line in input_file:
                # Remove the "Card ID: " part
                rest_of_line = line.split(": ", 1)[1].removesuffix("\n")

                # Divide the line into winning numbers and the card numbers
                winning_numbers, card_numbers = rest_of_line.split(" | ")

                # Convert the winning numbers and card numbers to sets
                winning_numbers = set(winning_numbers.split())
                card_numbers = set(card_numbers.split())

                # Check how many winning numbers are in the card numbers
                matching_numbers = winning_numbers.intersection(card_numbers)

                # Add the card points to the total points based on the number of matching numbers
                points += 2 ** (len(matching_numbers) - 1) if matching_numbers else 0

            if print_output:
                print(f"Total points: {points}")
                sys.exit(0)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
