from typing import TYPE_CHECKING

from blessed import Terminal

if TYPE_CHECKING:
    from player import Player


class Display:
    def __init__(self, player: "Player"):
        self.term = Terminal()
        self.rows, self.cols = self.term.height, self.term.width
        print(f"Initial size: {self.rows} rows, {self.cols} cols")

        self.player: "Player" = player

    def evaluate_with_color(self, attempt: str) -> list[str]:
        res = [""] * len(attempt)

        known_indexes = []
        for i, (c_test, c_secret) in enumerate(
            zip(attempt, self.player.current_secret_word)
        ):
            if c_test == c_secret:
                res[i] = self.term.on_red_bold(c_test)
                known_indexes.append(i)

        secret_cpy = list(self.player.current_secret_word)
        for i, c_test in enumerate(attempt):
            if c_test in secret_cpy:
                if i not in known_indexes:
                    res[i] = self.term.on_yellow_bold(c_test)
                secret_cpy[secret_cpy.index(c_test)] = "_"
            else:
                res[i] = self.term.bold(c_test)

        return res

    def start(self):
        with self.term.fullscreen():
            print("Press 'q' to quit.")
            with self.term.cbreak(), self.term.hidden_cursor():
                while True:
                    self.display()
                    key = self.term.inkey(timeout=1)
                    if key.name == "KEY_RESIZE":
                        self.on_resize(self.term.height, self.term.width)
                    elif not key:
                        continue
                    elif key == "q" or key.name == "KEY_ESCAPE":
                        break
                    else:
                        self.on_key(key)

    def on_key(self, key):
        # print(f"Key: {repr(key)}", end="\r\n")
        print(self.term.black_on_white(key), end="\r\n")

    def on_resize(self, rows, cols):
        self.rows, self.cols = rows, cols
        print(f"Terminal resized to {rows} rows and {cols} cols")

    def display_attempts(self):
        # print(self.term.location(0, 0))
        n = len(self.player.current_secret_word)
        attempts = self.player.attempts
        for i in range(n):
            if i < len(attempts):
                print("│".join(self.evaluate_with_color(attempts[i])))
            else:
                print("│".join("_" * n))
            print("┼".join("─" * n))

    def display(self):
        print(self.term.home + self.term.on_blue + self.term.clear)
        self.display_attempts()
