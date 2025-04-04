
class SumSolution:
    
    def compute(self, x, y):
        if 0 <= x <= 100 and 0 <= y <= 100:
            return x + y
        else:
            raise ValueError("Both x and y must be between 0 and 100 inclusive.")
            # raise NotImplementedError()
