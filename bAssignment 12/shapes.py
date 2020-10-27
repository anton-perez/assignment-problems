import matplotlib.pyplot as plt

class Shape:
  def __init__(self, base, height, color):
    self.base = base
    self.height = height
    self.color = color
  
  def describe(self):
    print("Base:", self.base)
    print("Height:", self.height)
    print("Color:", self.color)
    print("Perimeter:", self.perimeter)
    print("Area:", self.area)
    print("Vertices:", self.vertices)
  
  def render(self):
    plt.clf()
    plt.style.use('bmh')
    plt.plot(
      [vertex[0] for vertex in self.vertices]+[0],
      [vertex[1] for vertex in self.vertices]+[0],
      color = self.color)
    plt.gca().set_aspect("equal")
    plt.savefig(self.__class__.__name__+'.png')


class Rectangle(Shape):
  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = 2*base + 2*height
    self.area = base*height
    self.vertices = [(0, 0), (base, 0), (base,height), (0, height)]
    

class RightTriangle(Shape):
  def __init__(self, base, height, color):
    super().__init__(base, height, color)
    self.perimeter = base + height + (base**2 + height**2)**0.5
    self.area = base*height/2
    self.vertices = [(0, 0), (base, 0), (0, height)]


class Square(Rectangle):

  def __init__(self, base, color):
    super().__init__(base, base, color)


rect = Rectangle(5,2,'red')
rect.describe()
rect.render()

tri = RightTriangle(5,2,'blue')
tri.describe()
tri.render()

sq = Square(5,'green')
sq.describe()
sq.render()