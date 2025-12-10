from display import Display
from player import Player

if __name__ == "__main__":
    player = Player()

    player.attempts = [
        "entree",
        "emport",
        "emerge",
        "epiler",
    ]
    player.current_secret_word = "epiler"

    display = Display(player)
    display.start()
