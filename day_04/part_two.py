import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            lines = input_file.readlines()

            # Initialize a dictionary to store the number of copies of each scratchcard
            scratchcards = {i: 1 for i in range(1, len(lines) + 1)}

            for i, line in enumerate(lines):
                # Remove the "Card ID: " part
                rest_of_line = line.split(": ", 1)[1].removesuffix("\n")

                # Divide the line into winning numbers and the card numbers
                winning_numbers, card_numbers = rest_of_line.split(" | ")

                # Convert the winning numbers and card numbers to sets
                winning_numbers = set(winning_numbers.split())
                card_numbers = set(card_numbers.split())

                # Check how many winning numbers are in the card numbers
                matching_numbers = winning_numbers.intersection(card_numbers)

                if len(matching_numbers) == 0:
                    continue

                # Update the scratchcards dictionary as many times as the number
                # of copies of the current scratchcard
                for _ in range(scratchcards[i + 1]):
                    for j in range(1, len(matching_numbers) + 1):
                        scratchcards[i + 1 + j] += 1

            # Calculate the total number of scratchcards
            total_scratchcards = sum(scratchcards.values())

            if print_output:
                print(f"The total number of scratchcards is: {total_scratchcards}")
                sys.exit(0)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
