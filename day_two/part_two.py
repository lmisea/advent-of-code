import sys
from game import Game


def main(print_output: bool = True):
    try:
        with open("input.txt") as input_file:
            lines = input_file.readlines()
            games: list[Game] = []

            for line in lines:
                # We create a new game object with the game_id and the max cubes
                game = Game(
                    id=int(line.split()[1].removesuffix(":")),
                )

                # Remove the "Game ID: " part
                rest_of_line = line.split(": ", 1)[1].removesuffix("\n")

                # Directly divide the rest of the line into a list of cubes divided by ; and then by ,
                hints = [data.split(", ") for data in rest_of_line.split("; ")]

                # We iterate over the hints and update the max cubes for each color
                for hint in hints:
                    for cube in hint:
                        amount, color = cube.split(" ")
                        if color == "red":
                            game.update_max_red_cubes(int(amount))
                        elif color == "green":
                            game.update_max_green_cubes(int(amount))
                        elif color == "blue":
                            game.update_max_blue_cubes(int(amount))

                # We add the game to the list of games
                games.append(game)

            # We calculate the sum of the power of game sets (max_red_cubes * max_green_cubes * max_blue_cubes)
            game_power_sum = sum(
                game.get_max_red_cubes()
                * game.get_max_green_cubes()
                * game.get_max_blue_cubes()
                for game in games
            )

            if print_output:
                print(f"Sum of all game powers: {game_power_sum}")
                sys.exit(0)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
