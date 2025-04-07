
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
    # calculate the total checkout price
    # item A: 50, B: 30, C: 20, D: 15, E: 40, F: 10
    # special offers:
        # 5A 200, 3A 130,
        # 2B for 45
        # 2E get 1B free
        # 2F get 1F free
    # illegal input returns -1

        # count_A = 0
        # count_B = 0
        # count_C = 0
        # count_D = 0
        # count_E = 0
        # count_F = 0
        prices = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 15]
        count = [0]*26
        total_price = 0

        # count the number of each item
        for item in skus:
            if ord(item) < 65 or ord(item) > 90:
                return -1
            count[ord(item) - 65] += 1
        # for item in skus:
        #     if item == "A":
        #         count_A += 1
        #     elif item == "B":
        #         count_B += 1
        #     elif item == "C":
        #         count_C += 1
        #     elif item == "D":
        #         count_D += 1
        #     elif item == "E":
        #         count_E += 1
        #     elif item == "F":
        #         count_F += 1
        #     else:
        #         return -1
        
        # calculate the total price
        free_B = count[ord("E") - 65] // 2
    
        # check for 5A's, 3A's and A's
        if count_A >= 5:
            special_offer_5A = count_A // 5 * 200
            if count_A % 5 >= 3:
                special_offer_3A = (count_A % 5) // 3 * 130
                price_A = count_A % 5 % 3 * 50
            else:
                special_offer_3A = 0
                price_A = count_A % 5 * 50
        else:
            if count_A >= 3:
                special_offer_5A = 0
                special_offer_3A = count_A // 3 * 130
                price_A = count_A % 3 * 50
            else:
                special_offer_5A, special_offer_3A = 0, 0
                price_A = count_A * 50

        # check if there are more free B's than B's in the cart
        if free_B > count_B:
            price_B, special_offer_B = 0, 0
        else:
            special_offer_B = (count_B - free_B) // 2 * 45
            price_B = (count_B - free_B) % 2 * 30

        price_C = count_C * 20

        price_D = count_D * 15

        price_E = count_E * 40

        if count_F >= 3:
            special_offer_F = 2 * (count_F // 3) * 10
            price_F = count_F % 3 * 10
        else:
            special_offer_F = 0
            price_F = count_F * 10

        total_price = special_offer_5A + special_offer_3A + price_A + special_offer_B + price_B + price_C + price_D + price_E + special_offer_F + price_F

        return total_price

