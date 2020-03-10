from effects import effect
from modifiers import modifier


class status_effect():
    """
    
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.modifiers = []
        self.effects = []

    def __repr__(self):
        return f"<Status Effect {self.name}>"