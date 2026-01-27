class Healable:
    def heal(self, amount: int):
        """ Erhöht die health des Objekts um amount. """
        self.set_health(self.get_health() + amount)

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
        self.__name = name
        self.__health = 0
        self.__power = 0

        self.set_health(health)
        self.set_power(power)

    def get_name(self):
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def get_power(self) -> int:
        return self.__power

    def set_health(self, value: int) -> None:
        """health darf nicht kleiner als 0 werden."""
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    def set_power(self, value: int) -> None:
        """power darf nicht negativ sein."""
        if value < 0:
            self.__power = 0
        else:
            self.__power = value

    def receive_damage(self, damage: int):
        """Reduziert health um damage. Health fällt nicht unter 0."""
        # Schaden ist positiv → health sinkt
        new_health = self.get_health() - damage
        self.set_health(new_health)

    def attack(self, target: "Character"):
        """Greift einen anderen Character an und fügt ihm Schaden zu."""
        print(f"{self.get_name()} attacks {target.get_name()} for {self.get_power()} damage.")
        target.receive_damage(self.get_power())

class Monster(Character):
    """ Monster erbt von Character und kann in Rage gehen. """

    def __init__(self, name: str, health: int, power: int):
        """ Initialisiert Monster mit super().__init__(). """
        super().__init__(name, health, power)
        self.base_power = power  # Original-Power speichern für rage()

    def rage(self, rage: bool):
        """ Wenn True: Power verdoppelt sich. Wenn False: zurück zu Original. """
        if rage:
            self.set_power(self.base_power * 2)
        else:
            self.set_power(self.base_power)

class Player(Character):
    """ Spieler erbt von Character und hat ein Level. """

    def __init__(self, name: str, level: int = 1, health: int = 3, power: int = 1):
        """ Initialisiert Player mit Standardwerten aus der Aufgabe. """
        super().__init__(name, health, power)
        self.__level = 1

    def get_level(self) -> int:
        return self.__level

    def set_level(self, value: int) -> None:
        if value < 1:
            self.__level = 1
        else:
            self.__level = value

    def level_up(self):
        """ Erhöht das Level um 1. """
        self.set_level(self.get_level() + 1)
        print(f"{self.get_name()} has reached {self.get_level()}.")

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
        self.__mana = 10

    def get_mana(self):
        return self.__mana

    def set_mana(self, value: int) -> None:
        if value < 0:
            self.__mana = 0
        else:
            self.__mana = value

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

print(c1.get_name(), c1.get_health(), c1.get_power())
print(m1.get_name(), m1.get_health(), m1.get_power())
print(player1.get_name(), player1.get_health(), player1.get_power(), player1.get_level())
print(warrior1.get_name(), warrior1.get_health(), warrior1.get_power(), warrior1.get_level())
print(mage1.get_name(), mage1.get_health(), mage1.get_power(), mage1.get_level(), mage1.get_mana())
print(cleric1.get_name(), cleric1.get_health(), cleric1.get_power(), cleric1.get_level())
print(dwarf1.get_name(), dwarf1.get_health(), dwarf1.get_power())
print(elf1.get_name(), elf1.get_health(), elf1.get_power())

c1.receive_damage(5)
print("nach Schaden: ", c1.get_health())
c1.receive_damage(10)
print("nicht unter 0: ", c1.get_health())

m1.rage(True)
print(f"{m1.get_name()} wütend: ", m1.get_power())
m1.rage(False)
print(f"{m1.get_name()} ruhig: ", m1.get_power())

player1.level_up()

print("Vor Angriff: ", m1.get_health())
player1.attack(m1)
print("Nach Angriff: ", m1.get_health())

print(f"Gegner: {orc1.get_name()}, HP: {orc1.get_health()}, Power: {orc1.get_power()}")
orc1.rage(True)
print(f"Ork wütend - Power: {orc1.get_power()}")
player1.attack(orc1)
print(f"Nach Angriff - {orc1.get_name()} HP: {orc1.get_health()}")

print(f"Boss: {boss01.get_name()}, HP: {boss01.get_health()}, Power: {boss01.get_power()}, Mana: {boss01.mana}")
boss01.receive_damage(10)
print(f"Nach Schaden: {boss01.get_health()}")
boss01.heal(5)
print(f"Nach Heilung: {boss01.get_health()}")
boss01.cast_spell(player1, cost=5, damage=3)
print(f"Boss-Mana nach Zauber: {boss01.mana}")
print(f"Player-HP nach Zauber: {player1.get_health()}")