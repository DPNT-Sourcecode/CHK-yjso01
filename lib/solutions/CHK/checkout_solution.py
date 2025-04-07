
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 15]
        count = [0]*26
        total_price = 0

        # count the number of each item
        for item in skus:
            if ord(item) < 65 or ord(item) > 90:
                return -1
            count[ord(item) - 65] += 1
        
        # calculate the total price through the special offers----Main part-----
        # 2B for 45 and 2E get 1B free offer
        count_E = count[ord("E") - 65]
        count_B = count[ord("B") - 65]

        free_B = count_E // 2

        if free_B > count_B:
            price_B, special_offer_B = 0, 0
        else:
            special_offer_B = (count_B - free_B) // 2 * 45
            price_B = (count_B - free_B) % 2 * 30

        # 5A's for 200 and 3A's for 130 offer
        count_A = count[ord("A") - 65]

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

        # 2F get one F free offer
        count_F = count[ord("F") - 65]

        if count_F >= 3:
            special_offer_F = 2 * (count_F // 3) * 10
            price_F = count_F % 3 * 10
        else:
            special_offer_F = 0
            price_F = count_F * 10

        # 5H for 45 and 10H for 80 offer
        count_H = count[ord("H") - 65]

        if count_H >= 10:
            special_offer_10H = count_H // 10 * 80
            if count_H % 10 >= 5:
                special_offer_5H = (count_H % 10) // 5 * 45
                price_H = count_H % 10 % 5 * 10
            else:
                special_offer_5H = 0
                price_H = count_H % 10 * 10
        else:
            if count_H >= 5:
                special_offer_10H = 0
                special_offer_5H = count_H // 5 * 45
                price_H = count_H % 5 * 10
            else:
                special_offer_10H, special_offer_5H = 0, 0
                price_H = count_H * 10

        # 2k for 150 offer
        count_K = count[ord("K") - 65]
        if count_K >= 2:
            special_offer_2K = count_K // 2 * 150
            price_K = count_K % 2 * 80
        else:
            special_offer_2K = 0
            price_K = count_K * 80

        # 3N get one M free
        count_N = count[ord("N") - 65]
        count_M = count[ord("M") - 65]
        if count_N >= 3:
            special_offer_3N = count_N // 3 * 40
            price_M = count_M - count_N // 3
            if price_M < 0:
                price_M = 0
        else:
            special_offer_3N = 0
            price_M = count_M

        total_price = special_offer_5A + special_offer_3A + price_A + special_offer_B + price_B + price_C + price_D + price_E + special_offer_F + price_F

        return total_price




