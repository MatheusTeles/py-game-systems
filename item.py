class item():
    def __init__(self, name: str, rarity: str):
        self.name = name
        self.rarity = rarity

    def __repr__(self):
        return f"<{self.rarity} Item {self.name}>"


class equipable(item):

    def __init__(self, name: str, rarity: str, _type: str, stats: dict, status_effects: list):
        super().__init__(name, rarity)
        self.type = _type
        self.stats = stats
        self.status_effects = status_effects

    def __repr__(self):
        return f"<{self.rarity} {self.type} Equipment {self.name}>"
