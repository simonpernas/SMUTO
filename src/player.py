from client import Client


class Player:
    def __init__(self, name: str = "Player"):
        self.name = name
        self.client: "Client | None" = None

        self.current_secret_word: str = ""
        self.attempts: list[str] = []
