from solutions.SUM.sum_solution import SumSolution

class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(0, 100) == 0
        assert SumSolution().compute(101, 0) == 100
        assert SumSolution().compute(0, 101) == 100
        assert SumSolution().compute(101, 101) == 200
        assert SumSolution().compute(-1, 50) == 100
        assert SumSolution().compute(50, -1) == 100
        assert SumSolution().compute(-5, -5) == 100

