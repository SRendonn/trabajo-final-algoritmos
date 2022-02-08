from models.Punto import Punto

class Domiciliario(Punto):

    def __init__(self, x : int, y : int) -> None:
        super().__init__(x, y)

    def __str__(self):
        return "Domiciliario - (x={}, y={})".format(self.get_x(), self.get_y())
