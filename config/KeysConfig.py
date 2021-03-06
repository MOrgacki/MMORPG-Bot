

from config.Config import Config


class KeysConfig(Config):
    """Class contains bunch of getters to specific KEYS"""
    
    @property
    def get_attack_key(self):
        return self.get_property('attack_key')

    @property
    def get_chase_key(self):
        return self.get_property('chase_key')

    @property
    def get_high_hp_key(self):
        return self.get_property('high_hp_key')

    @property
    def get_low_hp_key(self):
        return self.get_property('low_hp_key')

    @property
    def get_mana_refill_key(self):
        return self.get_property('mana_refill_key')

    @property
    def get_food_key(self):
        return self.get_property('food_key')

    @property
    def get_three_monsters_key(self):
        return self.get_property('three_monsters_key')

    @property
    def get_two_monsters_key(self):
        return self.get_property('two_monsters_key')

    @property
    def get_two_monsters_key_2(self):
        return self.get_property('two_monsters_key_2')
    
    @property
    def get_three_monsters_key_strong(self):
        return self.get_property('three_monsters_key_strong')

