def f(x):
    return (x-1)**2 * (x-2) * (x-3)

def df(x):
    return 2*(x-1)*(x-2)*(x-3) + (x-1)**2*(x-3) + (x-1)**2*(x-2) + (x-2)*(x-3)*(2*x-5)

def newton_raphson(x0, tol, max_iter):
    x1 = x0 - f(x0)/df(x0)
    iterasyon_sayisi = 1
    while abs(x1 - x0) > tol and iterasyon_sayisi < max_iter:
        x0 = x1
        x1 = x0 - f(x0)/df(x0)
        iterasyon_sayisi += 1
    if iterasyon_sayisi == max_iter:
        print("Maksimum iterasyon sayısına ulaşıldı.")
    return x1, iterasyon_sayisi

# başlangıç noktasını x0 = 2 olarak belirleyelim, toleransı 0.0001 ve maksimum iterasyon sayısını 100 olarak ayarlayalım
x_opt, iterasyon_sayisi = newton_raphson(2, 0.0001, 100)

# x_opt ve iterasyon sayısını yazdıralım
print("Minimum değer: ", f(x_opt), "x değeri: ", x_opt, "iterasyon sayısı: ", iterasyon_sayisi)