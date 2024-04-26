import random
import curses

class SnakeGame:
    def __init__(self, height=20, width=60):
        self.height = height
        self.width = width
        self.snake = [(height // 2, width // 2)]
        self.direction = curses.KEY_RIGHT
        self.food = self._generate_food()

    def _generate_food(self):
        while True:
            food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
            if food not in self.snake:
                return food

    def _move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + (self.direction == curses.KEY_DOWN) - (self.direction == curses.KEY_UP),
                    head[1] + (self.direction == curses.KEY_RIGHT) - (self.direction == curses.KEY_LEFT))
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def _check_collision(self):
        head = self.snake[0]
        if (head in self.snake[1:] or
            head[0] in [0, self.height-1] or
            head[1] in [0, self.width-1]):
            return True
        return False

    def _draw(self, window):
        window.clear()
        window.border(0)
        window.addstr(self.food[0], self.food[1], '*')
        for i, (y, x) in enumerate(self.snake):
            if i == 0:
                window.addch(y, x, '#')
            else:
                window.addch(y, x, 'o')

    def play(self):
        curses.initscr()
        win = curses.newwin(self.height, self.width, 0, 0)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border(0)
        win.timeout(100)

        while True:
            self._draw(win)
            next_key = win.getch()
            if next_key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
                if (next_key == curses.KEY_RIGHT and self.direction != curses.KEY_LEFT or
                    next_key == curses.KEY_LEFT and self.direction != curses.KEY_RIGHT or
                    next_key == curses.KEY_UP and self.direction != curses.KEY_DOWN or
                    next_key == curses.KEY_DOWN and self.direction != curses.KEY_UP):
                    self.direction = next_key
            self._move_snake()
            if self._check_collision():
                break

        win.addstr(self.height // 2, self.width // 2 - 5, 'Game Over')
        win.refresh()
        curses.curs_set(1)
        win.getch()
        curses.endwin()

# Run the game
if __name__ == '__main__':
    game = SnakeGame()
    game.play()
