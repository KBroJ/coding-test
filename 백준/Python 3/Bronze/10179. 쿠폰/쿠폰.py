def coupon(F):

    for i in range(F):
        f_value = float(input()) * 0.8

        print(f"${f_value:.2f}")

F = int(input())
coupon(F)