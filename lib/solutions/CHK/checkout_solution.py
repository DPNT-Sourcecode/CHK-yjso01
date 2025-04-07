
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 50]
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
        price_E = count_E * 40

        if free_B > count_B:
            price_B, special_offer_B = 0, 0
        else:
            special_offer_B = (count_B - free_B) // 2 * 45
            price_B = (count_B - free_B) % 2 * 30
        
        total_B = special_offer_B + price_B
        total_E = price_E
        total_price += total_B + total_E
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

        total_A = special_offer_5A + special_offer_3A + price_A
        total_price += total_A
        # 2F get one F free offer
        count_F = count[ord("F") - 65]

        if count_F >= 3:
            special_offer_F = 2 * (count_F // 3) * 10
            price_F = count_F % 3 * 10
        else:
            special_offer_F = 0
            price_F = count_F * 10

        total_F = special_offer_F + price_F
        total_price += total_F
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

        total_H = special_offer_10H + special_offer_5H + price_H
        total_price += total_H
        # 2k for 150 offer
        count_K = count[ord("K") - 65]
        if count_K >= 2:
            special_offer_2K = count_K // 2 * 150
            price_K = count_K % 2 * 80
        else:
            special_offer_2K = 0
            price_K = count_K * 80

        total_K = special_offer_2K + price_K
        total_price += total_K
        # 3N get one M free
        count_N = count[ord("N") - 65]
        count_M = count[ord("M") - 65]

        if count_N >= 3:
            free_M = count_N // 3
            price_N = count_N * 40
            if free_M > count_M:
                price_M, special_offer_M = 0, 0
            else:
                price_M = (count_M - free_M) * 15
                special_offer_M = 0
        else:
            price_M = count_M * 15
            special_offer_M = 0
            price_N = count_N * 40

        total_N = price_N
        total_M = price_M + special_offer_M
        total_price += total_N + total_M
        # 5P for 200 offer
        count_P = count[ord("P") - 65]

        if count_P >= 5:
            special_offer_5P = count_P // 5 * 200
            price_P = count_P % 5 * 50
        else:
            special_offer_5P = 0
            price_P = count_P * 50

        total_P = special_offer_5P + price_P
        total_price += total_P
        # 3Q for 80 offer and 3R get one Q free offer
        count_Q = count[ord("Q") - 65]
        count_R = count[ord("R") - 65]

        free_Q = count_R // 3
        price_R = count_R * 50

        if free_Q > count_Q:
            price_Q, special_offer_Q = 0, 0
        else:
            special_offer_Q = (count_Q - free_Q) // 3 * 80
            price_Q = (count_Q - free_Q) % 3 * 30

        total_Q = special_offer_Q + price_Q
        total_R = price_R
        total_price += total_Q + total_R
        # 3U get one U free offer
        count_U = count[ord("U") - 65]
  
        if count_U >= 4:
            special_offer_U = 3 * (count_U // 4) * 40
            price_U = count_U % 4 * 40
        else:
            special_offer_U = 0
            price_U = count_U * 40

        total_U = special_offer_U + price_U
        total_price += total_U
        # 2V for 90, 3V for 130 offer
        count_V = count[ord("V") - 65]

        if count_V >= 3:
            special_offer_3V = count_V // 3 * 130
            if count_V % 3 >= 2:
                special_offer_2V = (count_V % 3) // 2 * 90
                price_V = count_V % 3 % 2 * 50
            else:
                special_offer_2V = 0
                price_V = count_V % 3 * 50
        else:
            if count_V >= 2:
                special_offer_3V = 0
                special_offer_2V = count_V // 2 * 90
                price_V = count_V % 2 * 50
            else:
                special_offer_3V, special_offer_2V = 0, 0
                price_V = count_V * 50

        total_V = special_offer_3V + special_offer_2V + price_V
        total_price += total_V

        # buy any 3 of (S,T,X,Y,Z) for 45 offer
        count_S = count[ord("S") - 65]
        s_price = prices[ord("S") - 65]

        count_T = count[ord("T") - 65]
        t_price = prices[ord("T") - 65]

        count_X = count[ord("X") - 65]
        x_price = prices[ord("X") - 65]

        count_Y = count[ord("Y") - 65]
        y_price = prices[ord("Y") - 65]

        count_Z = count[ord("Z") - 65]
        z_price = prices[ord("Z") - 65]

        item_group = [count for count in [count_S, count_T, count_X, count_Y, count_Z]]


        for i in range(26):
            if count[i] > 0 and chr(i+65) not in ["A", "B", "E", "F", "H", "K", "M", "N", "P", "Q", "R", "U", "V"]:
                total_price += count[i] * prices[i]

        return total_price


