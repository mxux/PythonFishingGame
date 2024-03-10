class rod:
    def __init__(self, name, description, price, line_length, hook_color, line_color):
        self.name = name
        self.description = description
        self.price = price
        self.line_length = line_length
        self.hook_color = hook_color
        self.line_color = line_color
    def __str__(self):
        return self.description
