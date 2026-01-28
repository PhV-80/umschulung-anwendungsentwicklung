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

# ============================================================================
# TEST-BEREICH - Demonstriert die Vererbung in Aktion
# ============================================================================

c1 = Character("Character 01", 10, 3)
m1 = Monster("Monster 01", 10, 4)
player1 = Player("Sascha")

print(c1.name, c1.health, c1.power)
print(m1.name, m1.health, m1.power)
print(player1.name, player1.health, player1.power, player1.level)

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