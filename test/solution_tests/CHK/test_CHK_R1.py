from solutions.CHK.checkout_solution import CheckoutSolution

def test_individual_items():
    assert CheckoutSolution().checkout("A") == 50
    assert CheckoutSolution().checkout("B") == 30
    assert CheckoutSolution().checkout("C") == 20
    assert CheckoutSolution().checkout("D") == 15
    assert CheckoutSolution().checkout("E") == 40

def test_special_offers():
    assert CheckoutSolution().checkout("AAA") == 130
    assert CheckoutSolution().checkout("BB") == 45
    assert CheckoutSolution().checkout("EEB") == 40

def test_combined_items():
    assert CheckoutSolution().checkout("ABCD") == 115
    assert CheckoutSolution().checkout("AABBC") == 165
    assert CheckoutSolution().checkout("AAABBB") == 205
    assert CheckoutSolution().checkout("EEBB") == 110
    assert CheckoutSolution().checkout("EEEBBBB") == 195

def test_invalid_input():
    assert CheckoutSolution().checkout("F") == -1
    assert CheckoutSolution().checkout("AABCF") == -1
    assert CheckoutSolution().checkout("123") == -1
    assert CheckoutSolution().checkout("") == 0
