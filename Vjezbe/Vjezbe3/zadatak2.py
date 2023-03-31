def funkcija(iteracija):
    a=5
    for i in range(iteracija):
        a=a+1/3
    for i in range(iteracija):
        a=a-1/3
    print(a)
funkcija(200)
funkcija(2000)
funkcija(20000)
#rezultat koji smo dobili razlikuje se ovisno o broju iteracija
#najmanji broj javlja se pri broju iteracija 200, srednji, ujedno i najbliži stvarnoj vrijednosti 5 javlja se pri broju iteracija 2000, a najveća pogreška i najveći broj javljaju se pri 20000 iteracija