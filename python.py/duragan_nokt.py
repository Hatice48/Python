import sympy as sym

# x1 ve x2 sembolleri tanımlanıyor
x1, x2 = sym.symbols('x1 x2')

# Fonksiyon tanımlanıyor
f = (x1 - 1) ** 2 + (x2 - 1) ** 2 - x1 * x2

# Gradient hesaplanıyor
gradient = [sym.diff(f, x) for x in (x1, x2)]

# Hessian hesaplanıyor
hessian = [[sym.diff(f, x1_, x2_) for x2_ in (x1, x2)] for x1_ in (x1, x2)]

# Durağan noktalar hesaplanıyor
durgan_noktalar = sym.solve(gradient, (x1, x2))

# Hessian'ın belirleyicisi hesaplanıyor
hessian_belirleyici = hessian[0][0] * hessian[1][1] - hessian[0][1] * hessian[1][0]

# Durağan noktaların tipleri belirleniyor
for durgan_nokta in durgan_noktalar:
    # Hessian'ın belirleyicisi 0 ise test yapılamaz
    if hessian_belirleyici == 0:
        print(f"Durağan nokta: {durgan_nokta}, tipi: bilinmiyor (Hessian belirleyici sıfır)")
    else:
        # Hessian'ın belirleyicisi 0'dan büyükse test yapılır
        # İkinci türev testi yapılır
        hessian_test = hessian.subs({x1: durgan_nokta[x1], x2: durgan_nokta[x2]})
        if hessian_test[0][0] > 0 and hessian_belirleyici > 0:
            print(f"Durağan nokta: {durgan_nokta}, tipi: minimum nokta")
        elif hessian_test[0][0] < 0 and hessian_belirleyici > 0:
            print(f"Durağan nokta: {durgan_nokta}, tipi: maksimum nokta")
        else:
            print(f"Durağan nokta: {durgan_nokta}, tipi: teğe nokta")