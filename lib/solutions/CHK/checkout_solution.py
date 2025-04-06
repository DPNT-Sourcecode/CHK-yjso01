
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
    # calculate the total checkout price
    # item A: 50, B: 30, C: 20, D: 15, E: 40
    # special offers:
        # 5A 200, 3A 130,
        # 2B for 45
        # 2E get 1B free
    # illegal input returns -1

        count_A = 0
        count_B = 0
        count_C = 0
        count_D = 0
        count_E = 0
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
            elif item == "E":
                count_E += 1
            else:
                return -1
        
        # calculate the total price
        special_offer_A = count_A // 3 * 130
        price_A = count_A % 3 * 50

        special_offer_B = count_B // 2 * 45
        price_B = count_B % 2 * 30

        price_C = count_C * 20

        price_D = count_D * 15

        special_offer_E = count_E // 2

        total_price = special_offer_A + price_A + special_offer_B + price_B + price_C + price_D

        return total_price
