class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie("red")
print("cookie one is", cookie_one.get_color())
print("cookie two is", cookie_two.get_color())
cookie_one.set_color("yellow")
print("cookie one now is", cookie_one.get_color())
print("cookie two still is", cookie_two.get_color())
