from utils import do_nothing
from equipment import equipment


class entity:

    ENTITY_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = entity.ENTITY_ID
        entity.ENTITY_ID += 1


class item(entity):

    def __init__(self, name: str):
        super().__init__(name)
        self.owner = None
        self.event_handlers = {}
        self.on_use_handler = do_nothing

    def on_use(self, origin: entity, target: entity):
        self.on_use_handler(origin, target)

    def __repr__(self):
        return f"<Item {self.name}>"


class character(entity):
    
    def __init__(self, name: str, equipment: equipment = None):
        super().__init__(name)
        self.inventory = []
        self.equipment = equipment
        self.status_effects = []
        self.event_handlers = {}
        self.base_stats = {}
        self.stats = {}
        self.dirty_stats = True
        self.dirty_status_effects = True
        self.gender = ''
        self.pronouns = ()

    def apply_status_effect(self, status_effect):
        self.status_effects.append(status_effect)
        self.dirty_stats = True

    def remove_status_effect(self, status_effect):
        self.status_effects.remove(status_effect)
        self.dirty_stats = True

    def calc_stats(self):
        ret = {}
        delta = {}

        for stat in self.base_stats:
            ret[stat] = self.base_stats[stat]
            delta[stat] = [0, 1.0]

        if self.equipment:
            equipment_stats = self.equipment.get_stats()

            for equipment_stat in equipment_stats:
                delta[equipment_stat][0] += equipment_stats[equipment_stat]

        for eff in self.status_effects:
            for mod in eff.modifiers:
                for stat in mod.stats:
                    if mod.stats[stat]['type'] == 'add':
                        delta[stat][0] += mod.stats[stat]['value']
                    if mod.stats[stat]['type'] == 'mul':
                        delta[stat][1] += mod.stats[stat]['value']

        for stat in ret:
            ret[stat] = (ret[stat] + delta[stat][0]) * delta[stat][1]

        return ret

    def get_stats(self):
        if self.dirty_stats:
            self.stats = self.calc_stats()
            self.dirty_stats = False
        return self.stats

    def obtain_item(self, item):
        item.owner = self
        self.inventory.append(item)

    def use_item(self, item, target: entity):
        item.on_use(self, target)

    def equip_equipable(self, equipable):
        if self.equipment.equip_item(equipable):
            if equipable.stats:
                self.dirty_stats = True
            if equipable.status_effects:
                self.dirty_status_effects = True
            for status in equipable.status_effects:
                self.apply_status_effect(status)

    def unequip_equipable(self, equipable):
       if self.equipment.unequip_item(equipable):
            if equipable.stats:
                self.dirty_stats = True
            if equipable.status_effects:
                self.dirty_status_effects = True
            for status in equipable.status_effects:
                self.remove_status_effect(status)

    def __repr__(self):
        return f"<Player {self.name}>"
