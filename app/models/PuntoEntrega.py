from models.Punto import Punto

class PuntoEntrega(Punto):

    def __init__(self, x : int, y : int) -> None:
        super().__init__(x, y)

    def __str__(self):
        return "Punto Entrega - (x={}, y={})".format(self.get_x(), self.get_y())