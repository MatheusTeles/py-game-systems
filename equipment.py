
class slot:

    def __init__(self, _type: str):
        self.type = _type
        self.item = None

    def __repr__(self):
        return f"<{self.type} Equipment Slot - {self.item.name if self.item is not None else 'Empty'}>"


class equipment:

    def __init__(self, slots: list = []):
        self.slots = slots
        self.dirty_stats = True
        self.stats = {'hp': 0, 'atk': 0, 'def': 0, 'spd': 0}
        self.dirty_status_effects = True
        self.status_effects = {}

    def get_stats(self):
        if self.dirty_stats:
            self.stats = self.calc_stats()
            self.dirty_stats = False
        return self.stats

    def calc_stats(self):
        ret = {}
        delta = {}

        for stat in self.stats:
            ret[stat] = 0
            delta[stat] = [0, 1.0]

        for slot in self.slots:
            if slot.item:
                for stat in slot.item.stats:
                    if slot.item.stats[stat]['type'] == 'add':
                        delta[stat][0] += slot.item.stats[stat]['value']
                    if slot.item.stats[stat]['type'] == 'mul':
                        delta[stat][1] += slot.item.stats[stat]['value']

        for stat in ret:
            ret[stat] = (ret[stat] + delta[stat][0]) * delta[stat][1]
        return ret

    def equip_item(self, item):
        for slot in self.slots:
            if item.type == slot.type:
                slot.item = item
                if item.stats:
                    self.dirty_stats = True
                if item.status_effects:
                    self.dirty_status_effects = True
                return True
        return False

    def unequip_item(self, item):
        for slot in self.slots:
            if item.type == slot.type:
                slot.item = None
                if item.stats:
                    self.dirty_stats = True
                if item.status_effects:
                    self.dirty_status_effects = True
                return True
        return False

    def __repr__(self):
        return f"{''.join([slot.__repr__() for slot in self.slots])}"