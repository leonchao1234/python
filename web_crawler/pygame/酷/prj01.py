class Player:

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        if damage > self.defense:
            self.health -= damage - self.defense
            return f"{self.name}受到了{damage}點傷害"
        else:
            return f"{self.name}成功抵擋傷害！！"


# Player1 = Player("茶碗蒸", 100, 2, 9)
# print(f"玩家名稱：{Player1.name}")
# print(f"玩家血量：{Player1.health}")
# print(f"玩家攻擊：{Player1.attack}")
# print(f"玩家防禦：{Player1.defense}")
# Player2 = Player("刺青男", 80, 5, 8)
# print(f"玩家名稱：{Player2.name}")
# print(f"玩家血量：{Player2.health}")
# print(f"玩家攻擊：{Player2.attack}")
# print(f"玩家防禦：{Player2.defense}")

# print(Player2.take_damage(Player1.attack))
# print(f"刺青男血量剩餘.{Player2.health}")


class Mage(Player):

    def __init__(self, name, health, attack, defense, magic_power):
        super().__init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self):
        self.magic_power -= 10
        return 20 + self.attack


class Warrior(Player):

    def __init__(self, name, health, attack, defense, armor):
        super().__init__(name, health, attack, defense)
        self.armor = armor

    def use_armor(self):
        self.health += self.armor
        return f"{self.name}使用裝甲恢復"


player1 = Warrior("戰士小明", 100, 15, 10, 5)  # 裡面包含了Player的物件，所以可以使用Player的方法
player2 = Mage("法師小華", 80, 10, 10, 20)

print(f"{player1.name}血量剩餘: {player1.health}")
print(player1.use_armor())
print(f"{player1.name}血量剩餘: {player1.health}")

print(f"{player2.name}目前魔力: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對{player1.name}施放魔法攻擊！")
print(f"{player2.name}目前魔力: {player2.magic_power}")
print(f"{player1.name}血量剩餘: {player1.health}")