class Character:
    def __init__(self, max_hp: int, max_armor: int, dmg: int, attackspeed: float):
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_armor = max_armor
        self.armor = max_armor
        self.dmg = dmg
        self.attackspeed = attackspeed

    def takedmg(self, amount: int):
        self.armor -= amount
        if self.armor < 0:
            takedmg_hp = 0 - self.armor
            self.hp -= takedmg_hp
            self.armor = 0
            if self.hp < 0:
                self.hp = 0

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            heal_armor = self.hp - self.max_hp
            self.armor += heal_armor
            self.hp = self.max_hp
            if self.armor > self.max_armor:
                self.armor = self.max_armor

    def attack(self, target: "Character"):
        target.takedmg(self.dmg)


class Warrior(Character):
    def __init__(self):
        super().__init__(max_hp=200, max_armor=200, dmg=10, attackspeed=1.5)


class Mage(Character):
    def __init__(self):
        super().__init__(max_hp=100, max_armor=100, dmg=20, attackspeed=2.0)


class Hunter(Character):
    def __init__(self):
        super().__init__(max_hp=150, max_armor=150, dmg=15, attackspeed=1.75)
