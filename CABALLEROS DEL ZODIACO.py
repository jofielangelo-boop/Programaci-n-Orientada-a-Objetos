
import random

class Caballerosdelzodiaco:
    def __init__(self, nombre, max_hp, defensa):
        self.nombre = nombre
        self.max_hp = max_hp
        self.hp = max_hp
        self.defensa = defensa

    def recibir_danio(self, danio):
        danio_real = max(1, danio - self.defensa)
        self.hp -= danio_real
        print(f"¡{self.nombre} recibió {danio_real} de daño!")
        if self.hp <= 0:
            print(f"¡{self.nombre} se desmayó!")

    def atacar(self, objetivo):
        danio = random.randint(10, 20)
        print(f"¡{self.nombre} ataca a {objetivo.nombre} por {danio} de daño!")
        objetivo.recibir_danio(danio)


class Regulusdeleo(Caballerosdelzodiaco):
    def __init__(self):
        super().__init__("REGULUS DE LEO", 50, 5)


class Radamantisdewebern(Caballerosdelzodiaco):
    def __init__(self):
        super().__init__("RADAMANTIS DE WEBERN", 60, 3)


def batalla(caballerodelzodiaco1, caballerodelzodiaco2):
    print(f"¡Un {caballerodelzodiaco2.nombre} Radamandtis apareció!")
    while caballerodelzodiaco1.hp > 0 and caballerodelzodiaco2.hp > 0:
        caballerodelzodiaco1.atacar(caballerodelzodiaco2)
        if caballerodelzodiaco2.hp <= 0:
            break

        caballerodelzodiaco2.atacar(caballerodelzodiaco1)
        if caballerodelzodiaco1.hp <= 0:
            break


regulusdeleo = Regulusdeleo()
radamantisdewebern = Radamantisdewebern()

batalla(regulusdeleo, radamantisdewebern)
