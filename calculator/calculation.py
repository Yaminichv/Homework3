class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def Output(self):
        return self.operation(self.a, self.b)