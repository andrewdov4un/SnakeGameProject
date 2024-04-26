import unittest
from snake_game import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = SnakeGame()

    def test_initialization(self):
        self.assertEqual(len(self.game.snake), 1)
        self.assertTrue(all(0 <= y < self.game.height and 0 <= x < self.game.width for y, x in self.game.snake))
        self.assertTrue(all(0 <= self.game.food[0] < self.game.height and 0 <= self.game.food[1] < self.game.width))
        self.assertNotEqual(self.game.snake[0], self.game.food)

    def test_move_snake(self):
        initial_snake = self.game.snake[:]
        initial_food = self.game.food
        self.game._move_snake()
        self.assertNotEqual(self.game.snake, initial_snake)
        self.assertTrue(all(0 <= y < self.game.height and 0 <= x < self.game.width for y, x in self.game.snake))
        if initial_food == self.game.food:
            self.assertEqual(len(self.game.snake), len(initial_snake) + 1)
        else:
            self.assertEqual(len(self.game.snake), len(initial_snake))

    def test_check_collision(self):
        self.assertFalse(self.game._check_collision())
        self.game.snake = [(0, 0)] * 3
        self.assertTrue(self.game._check_collision())
        self.game.snake = [(self.game.height-1, self.game.width-1)] * 3
        self.assertTrue(self.game._check_collision())

if __name__ == '__main__':
    unittest.main()
