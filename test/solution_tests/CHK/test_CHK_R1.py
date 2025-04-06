from solutions.CHK.checkout_solution import CheckoutSolution

def test_individual_items():
    assert CheckoutSolution().checkout("A") == 50
    assert CheckoutSolution().checkout("B") == 30
    assert CheckoutSolution().checkout("C") == 20
    assert CheckoutSolution().checkout("D") == 15

def test_special_offers():
    assert CheckoutSolution().checkout("AAA") == 130
    assert CheckoutSolution().checkout("BB") == 45

def test_combined_items():
    assert CheckoutSolution().checkout("ABCD") == 115
    assert CheckoutSolution().checkout("AABBC") == 165
    assert CheckoutSolution().checkout("AAABBB") == 205 

def test_invalid_input():
    assert CheckoutSolution().checkout("E") == -1
    assert CheckoutSolution().checkout("AABCE") == -1
    assert CheckoutSolution().checkout("123") == -1
    assert CheckoutSolution().checkout("") == 0