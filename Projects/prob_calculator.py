import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def draw(self, number_of_balls_to_draw):
        drawn_balls = []

        if number_of_balls_to_draw >= len(self.contents):
            return self.contents

        for i in range(number_of_balls_to_draw):
            random_index = random.randint(0, len(self.contents) - 1)
            ball = self.contents.pop(random_index)
            drawn_balls.append(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)

        # Check if each "color" has been drawn at least "number" of times
        success = 0
        for color, number in expected_balls.items():
            count = len(list(filter(lambda c: c == color, balls)))
            if count >= number:
                success += 1

        # All expected balls were found
        if success == len(expected_balls.keys()):
            successful_experiments += 1

    return successful_experiments / num_experiments


random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
