def takrorla(satrlar):
    yangi_satrlar = []
    for satr in satrlar:
        sozlar = satr.split()
        yangi_sozlar = [soz for soz in sozlar for _ in range(2)]
        yangi_satr = ' '.join(yangi_sozlar)
        yangi_satrlar.append(yangi_satr)
    return yangi_satrlar

satrlar = ["Men dasturchiman", "Python tilini bilaman", "Kod yozishni yaxshi ko'raman"]
print(takrorla(satrlar))
