class Healable:
    def heal(self, amount: int):
        """ Erhöht die health des Objekts um amount. """
        self.health += amount

class MagicUser:
    def __init__(self, mana: int = 10):
        self.mana = mana

    def cast_spell(self, target, cost: int, damage: int):
        """ Wirkt einen Zauber auf target, falls genug Mana vorhanden ist. """
        if self.mana < cost:
            print("Nicht genug Mana!")
            return
        self.mana -= cost
        target.receive_damage(damage)

class Character:
    """ Basisklasse für alle Spielfiguren. """

    def __init__(self, name: str, health: int, power: int):
        """ Initialisiert einen Character mit Name, Leben und Kraft. """
        self.name = name
        self.health = health
        self.power = power

    def receive_damage(self, damage: int):
        """ Reduziert health um damage. Health fällt nicht unter 0. """
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, target: "Character"):
        """ Greift einen anderen Character an und fügt ihm Schaden zu. """
        print(f"{self.name} attacks {target.name} for {self.power} damage.")
        target.receive_damage(self.power)

class Monster(Character):
    """ Monster erbt von Character und kann in Rage gehen. """

    def __init__(self, name: str, health: int, power: int):
        """ Initialisiert Monster mit super().__init__(). """
        super().__init__(name, health, power)
        self.base_power = power  # Original-Power speichern für rage()

    def rage(self, rage: bool):
        """ Wenn True: Power verdoppelt sich. Wenn False: zurück zu Original. """
        if rage:
            self.power = self.base_power * 2
        else:
            self.power = self.base_power

class Player(Character):
    """ Spieler erbt von Character und hat ein Level. """

    def __init__(self, name: str, level: int = 1, health: int = 3, power: int = 1):
        """ Initialisiert Player mit Standardwerten aus der Aufgabe. """
        super().__init__(name, health, power)
        self.level = level

    def level_up(self):
        """ Erhöht das Level um 1. """
        self.level += 1
        print(f"{self.name} has reached {self.level}.")

class Orc(Monster):
    """Orc erbt von Monster – Beispiel für Unterklassen-Spezialisierung."""

    def __init__(self, name: str):
        """Orks haben standardmäßig höhere Health und Power."""
        super().__init__(name, health=15, power=5)

class Dwarf(Monster):
    def __init__(self, name: str):
        """ Zwerge: robust, mittlere Power"""
        super().__init__(name, health=12, power=3)

class Elf(Monster):
    def __init__(self, name: str):
        """ Elfen: weniger Health, höhere Power."""
        super().__init__(name, health=8, power=4)

class BossMonster(Monster, Healable, MagicUser):
    def __init__(self, name: str):
        """ Monster Part init"""
        Monster.__init__(self, name, health=30, power=6)
        """ MagicUser Part init """
        MagicUser.__init__(self, mana=20)

class Warrior(Player):
    def __init__(self, name: str):
        """ Krieger: mehr Health, mehr Power"""
        super().__init__(name, level=1, health=5, power=3)

class Mage(Player):
    def __init__(self, name: str):
        """ Magier: weniger Health, mehr Power"""
        super().__init__(name, level=1, health=2, power=5)
        self.mana = 10

class Cleric(Player):
    def __init__(self, name: str):
        """Kleriker: ausgewogen, etwas mehr Health"""
        super().__init__(name, level=1, health=4, power=2)

# ============================================================================
# TEST-BEREICH - Demonstriert die Vererbung in Aktion
# ============================================================================

c1 = Character("Character 01", 10, 3)
m1 = Monster("Monster 01", 10, 4)
player1 = Player("Sascha")
orc1 = Orc("Gorbag")
dwarf1 = Dwarf("Gimli")
elf1 = Elf("Legolas")
boss01 = BossMonster("Balrog")
warrior1 = Warrior("Conan")
mage1 = Mage("Gandalf")
cleric1 = Cleric("Uther")

print(c1.name, c1.health, c1.power)
print(m1.name, m1.health, m1.power)
print(player1.name, player1.health, player1.power, player1.level)
print(warrior1.name, warrior1.health, warrior1.power, warrior1.level)
print(mage1.name, mage1.health, mage1.power, mage1.level, mage1.mana)
print(cleric1.name, cleric1.health, cleric1.power, cleric1.level)
print(dwarf1.name, dwarf1.health, dwarf1.power)
print(elf1.name, elf1.health, elf1.power)

c1.receive_damage(5)
print("nach Schaden: ", c1.health)
c1.receive_damage(10)
print("nicht unter 0: ", c1.health)

m1.rage(True)
print(f"{m1.name} wütend: ", m1.power)
m1.rage(False)
print(f"{m1.name} ruhig: ", m1.power)

player1.level_up()

print("Vor Angriff: ", m1.health)
player1.attack(m1)
print("Nach Angriff: ", m1.health)

print(f"Gegner: {orc1.name}, HP: {orc1.health}, Power: {orc1.power}")
orc1.rage(True)
print(f"Ork wütend - Power: {orc1.power}")
player1.attack(orc1)
print(f"Nach Angriff - {orc1.name} HP: {orc1.health}")

print(f"Boss: {boss01.name}, HP: {boss01.health}, Power: {boss01.power}, Mana: {boss01.mana}")
boss01.receive_damage(10)
print(f"Nach Schaden: {boss01.health}")
boss01.heal(5)
print(f"Nach Heilung: {boss01.health}")
boss01.cast_spell(player1, cost=5, damage=3)
print(f"Boss-Mana nach Zauber: {boss01.mana}")
print(f"Player-HP nach Zauber: {player1.health}")