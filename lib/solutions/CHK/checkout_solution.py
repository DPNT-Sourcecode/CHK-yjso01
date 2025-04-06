
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
    # calculate the total checkout price
    # item A: 50, B: 30, C: 20, D: 15
    # special offers: 3A 130, 2B for 45
    # illegal input returns -1

        count_A = 0
        count_B = 0
        count_C = 0
        count_D = 0
        total_price = 0

        # count the number of each item
        for item in skus:
            if item == "A":
                count_A += 1
            elif item == "B":
                count_B += 1
            elif item == "C":
                count_C += 1
            elif item == "D":
                count_D += 1
            else:
                return -1
        
        # calculate the total price



