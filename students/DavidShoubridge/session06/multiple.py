class Human(object):
    """Can a class inherit from a super and a sub-class? Not working, \
    unless I'm writing this wrong, it doesnt seem to work."""

    def __init__(self, arms, legs, eyes):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes


class Avenger(Human):
    def __init__(self, power, costume):
        self.power = power
        self.costume = costume


class Hero(Human, Avenger):

    def __init__(self, name):
        self.name = name
        Human.__init__(self, 2, 2, 2)
        Avenger.__init__(self, "Super-strength", "Tights")

print(vars(Hero))
