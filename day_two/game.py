class Game:
    def __init__(
        self,
        id: int,
        max_red_cubes: int = None,
        max_green_cubes: int = None,
        max_blue_cubes: int = None,
    ):
        self.id = id
        self.max_red_cubes = max_red_cubes
        self.max_green_cubes = max_green_cubes
        self.max_blue_cubes = max_blue_cubes

    def update_max_red_cubes(self, red_cubes: int):
        if self.max_red_cubes is None:
            self.max_red_cubes = red_cubes
        elif red_cubes > self.max_red_cubes:
            self.max_red_cubes = red_cubes

    def update_max_green_cubes(self, green_cubes: int):
        if self.max_green_cubes is None:
            self.max_green_cubes = green_cubes
        elif green_cubes > self.max_green_cubes:
            self.max_green_cubes = green_cubes

    def update_max_blue_cubes(self, blue_cubes: int):
        if self.max_blue_cubes is None:
            self.max_blue_cubes = blue_cubes
        elif blue_cubes > self.max_blue_cubes:
            self.max_blue_cubes = blue_cubes

    def get_id(self):
        return self.id

    def get_max_red_cubes(self):
        return self.max_red_cubes

    def get_max_green_cubes(self):
        return self.max_green_cubes

    def get_max_blue_cubes(self):
        return self.max_blue_cubes

    def __str__(self):
        return f"Game {self.id}: {self.max_red_cubes} red, {self.max_green_cubes} green, {self.max_blue_cubes} blue"
