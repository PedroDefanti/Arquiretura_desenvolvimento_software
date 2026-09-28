from abc import ABC, abstractmethod



class Renderer(ABC):

    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_square(self, side: float):
        pass

class VectorRenderer(Renderer):
    

    def render_circle(self, radius: float):
        print(f"Desenhando um círculo de raio {radius} usando linhas vetoriais.")

    def render_square(self, side: float):
        print(f"Desenhando um quadrado de lado {side} usando linhas vetoriais.")


class RasterRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f"Renderizando pixels para formar um círculo de raio {radius}.")

    def render_square(self, side: float):
        print(f"Renderizando pixels para preencher um quadrado de lado {side}.")



class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):
        pass



class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor
        print(f"Círculo redimensionado para o raio: {self.radius}")


class Square(Shape):
    def __init__(self, renderer: Renderer, side: float):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor: float):
        self.side *= factor
        print(f"Quadrado redimensionado para o lado: {self.side}")

if __name__ == "__main__":
    
    vector = VectorRenderer()
    raster = RasterRenderer()

    print("--- Combinação 1: Círculo com Renderizador Vetorial ---")
    circle_vector = Circle(vector, radius=5.0)
    circle_vector.draw()
    circle_vector.resize(2.0)
    circle_vector.draw()

    print("\n--- Combinação 2: Quadrado com Renderizador Raster ---")
    square_raster = Square(raster, side=10.0)
    square_raster.draw()

    print("\n--- Combinação Cruzada Flexível: Círculo com Renderizador Raster ---")
    circle_raster = Circle(raster, radius=3.5)
    circle_raster.draw()