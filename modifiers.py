class modifier:
    """
        Class used to describe a buff/debuff that modifies stats (and stats only).\n
        Parameters:\n
              Name - name of the modifier.\n
              Stats - dictionary containing the stat to be modified, its value and if its an additive or multiplicative modifier.\n
        The Stats dictionary is structured like the example below, where 'add' stands for additive and 'mul' stands for multiplicative:

            stats = { 'hp'  : {'value' : 1000, 
                               'type': 'add'} , 
                      'spd' : {'value' : -0.8, 
                               'type': 'mul'} 
                    }  

        In the example above, the modifier gives a flat +1000 increase to health, and a 80% speed decrease.
    """

    def __init__(self, name: str, stats: dict):
        self.name = name
        self.stats = stats

    def __repr__(self):
        return f"<Modifier {self.name}>"
