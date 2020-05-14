
class Role(object):
    def __init__(self, name, hp, level):
        self.name = name
        self.max = hp
        self._hp = hp
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        # return 'Name:{}\t HP: {} \t Level:{}'.format(self.name, self._hp, self.level)
        return 'Name:%s \t HP: %3d \t Level: %2d' % (self.name, self._hp, self.level)
