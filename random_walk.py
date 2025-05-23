import random

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=50000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            # Decide direction and distance
            x_step = random.choice([1, -1, 0])
            y_step = random.choice([1, -1, 0])

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate next x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)