from abc import ABC, abstractmethod


class py(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @abstractmethod
    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    @abstractmethod
    def dibujar(self):
        return {"x": self.x, "y": self.y}


class Punto(py):
    def mover(self, dx: int, dy: int):
        super().mover(dx, dy)

    def dibujar(self):
        return f"Punto(x={self.x}, y={self.y})"


if __name__ == "__main__":
    punto = Punto(3, 4)
    print(punto.dibujar())
    punto.mover(2, -1)
    print(punto.dibujar())

