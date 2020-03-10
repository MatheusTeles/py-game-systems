from utils import do_nothing
import entities


class effect():

    """
    
    """
    def __init__(self, name: str, origin: entities.entity):

        self.origin = origin

        self.on_deal_damage_handler = do_nothing
        self.on_receive_damage_handler = do_nothing

        self.on_heal_self_handler = do_nothing
        self.on_heal_other_handler = do_nothing

        self.on_get_in_range_handler = do_nothing
        self.on_leave_range_handler = do_nothing

        self.on_use_item_handler = do_nothing
        self.on_item_used_on_self_handler = do_nothing

        def on_deal_damage(self, data: dict):
            self.on_deal_damage_handler(self.origin, data)

        def on_receive_damage(self, data: dict):
            self.on_receive_damage_handler(self.origin, data)

        def on_heal_self(self, data: dict):
            self.on_heal_self_handler(self.origin, data)

        def on_heal_other(self, data: dict):
            self.on_heal_other_handler(self.origin, data)

        def on_get_in_range(self, data: dict):
            self.on_get_in_range_handler(self.origin, data)

        def on_leave_range(self, data: dict):
            self.on_leave_range_handler(self.origin, data)

        def on_use_item(self, data: dict):
            self.on_use_item_handler(self.origin, data)

        def on_item_used_on_self(self, data: dict):
            self.on_item_used_on_self_handler(self.origin, data)

    def __repr__(self):
        return f"<Effect {self.name}>"
