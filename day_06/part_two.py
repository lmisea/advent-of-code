import sys


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            lines = input_file.read().splitlines()

            # Remove the Time: and Distance: prefixes and split by spaces
            times = lines[0].split(":")[1].split()
            records = lines[1].split(":")[1].split()

            # Join the time and distance values into single numbers
            time = int("".join(times))
            record = int("".join(records))

            ways_to_beat_the_record = 0

            for hold in range(1, time // 2 + 1):
                # The speed is hold because that's the time the bot is accelerating
                dist = (time - hold) * hold
                if dist > record:
                    if time % 2 == 0 and hold == time // 2:
                        ways_to_beat_the_record += 1
                    else:
                        ways_to_beat_the_record += 2

            if print_output:
                print("The total ways to beat the record are:", ways_to_beat_the_record)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
