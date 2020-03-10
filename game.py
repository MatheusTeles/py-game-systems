from effects import effect
from entities import entity, character
from item import item, equipable
from modifiers import modifier
from status_effects import status_effect
from equipment import slot, equipment


def wooden_staff_use(origin: entity, target: entity):
    print(f"{origin.name} uses the Wooden Staff. Nothing interesting happens.")


def potion_use(origin: entity, target: entity):
    target.base_stats['hp'] += 30
    print(
        f"{origin.name} uses Potion on {f'{origin.pronouns[1]}self' if origin==target else target.name}, restoring 30 health.")


if __name__ == "__main__":

    player1 = character('Rann')
    player1.base_stats = {'hp': 100, 'atk': 30, 'def': 30, 'spd': 30}
    player1.gender = 'Male'
    player1.pronouns = ('he', 'him')

    player2 = character('Anne')
    player2.base_stats = {'hp': 100, 'atk': 30, 'def': 30, 'spd': 30}
    player2.gender = 'Female'
    player2.pronouns = ('she', 'her')

    player3 = character('Sylas')
    player3.base_stats = {'hp': 100, 'atk': 30, 'def': 30, 'spd': 30}
    player3.gender = 'Nonbinary'
    player3.pronouns = ('xe', 'xer')

    m = modifier('curse', {'spd': {'value': -0.4, 'type': 'mul'},
                           'hp':  {'value': -50,  'type': 'add'}
                           })

    s = status_effect('Curse',
                      'Reduces player\'s max hp by 50 and speed by 40%')
    s.modifiers.append(m)

    m2 = modifier('blessing of kings', {'hp': {'value': 0.10, 'type': 'mul'},
                                        'atk': {'value': 0.10, 'type': 'mul'},
                                        'def': {'value': 0.10, 'type': 'mul'},
                                        'spd': {'value': 0.10, 'type': 'mul'}
                                        })

    s2 = status_effect('Blessing of Kings', 'Raises every status by 10%')
    s2.modifiers.append(m2)

    i = equipable('Cursed Wooden Staff', 'Common', 'Main Hand', {
                  'atk': {'value': 10, 'type': 'add'},
                  'hp': {'value': 5, 'type': 'add'},
                  'def': {'value': 3, 'type': 'add'}}, [s])
    i.on_use_handler = wooden_staff_use

    i2 = equipable('Ring of Kings', 'Legendary', 'Ring', {}, [s2])

    j = item('Potion', 'Common')
    j.on_use_handler = potion_use

    print(player1.get_stats())

    player1.equipment = equipment([slot('Main Hand'), slot('Ring')])

    player1.equip_equipable(i)
    print(f'Item equipped {i}')
    print(player1.get_stats())

    player1.equip_equipable(i2)
    print(f'Item equipped {i2}')
    print(player1.get_stats())
        
    print(player1.equipment)

    player1.unequip_equipable(i)
    print(f'Item unequipped {i}')
    print(player1.get_stats())
            
    player1.unequip_equipable(i2)
    print(f'Item unequipped {i2}')
    print(player1.get_stats())