import math

# Verilen fonksiyonu tanımladık
def f(x):
    return (x - 1) ** 2 * (x - 2) * (x - 3)

# Altın oran değeri hesaplandı
phi = (1 + math.sqrt(5)) / 2

# Başlangıç noktaları 
a = 0
b = 4

# Tolerans aralığı 
tol = 0.0001

# Altın oran yöntemi ile minimum noktayı hesapladık
iterasyon = 0
while abs(b - a) > tol:
    iterasyon += 1
    
    # Birinci ve ikinci noktaların hesaplanması
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    
    # Minimum noktanın hangi aralıkta olduğuna göre aramanın yapılması
    if f(x1) < f(x2):
        b = x2
    else:
        a = x1
    
    # Her iterasyonda minimum nokta, aralık ve x1, x2, f(x1), f(x2) yazdırılıyor
    print(f"Iterasyon {iterasyon}: Minimum nokta {round((a + b) / 2, 4)}, aralık {round(abs(b - a), 4)}, x1 = {round(x1, 4)}, x2 = {round(x2, 4)}, f(x1) = {round(f(x1), 4)}, f(x2) = {round(f(x2), 4)}")