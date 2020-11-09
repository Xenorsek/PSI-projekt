#Zadanie1
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Sebastian"
nazwisko = "Krzynówek"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter1 = tekst.count(litera_1)
liczba_liter2 = tekst.count(litera_2)
print(f"W tekście jest {liczba_liter1} liter 'b' oraz {liczba_liter2} liter 'y'")
#Zadanie4
zmienna_typu_string = "Konstytucja"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.find(imie[5]))
#Zadanie5
print(f'{imie[:: -1]} {nazwisko[::-1]}')
#Zadanie6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
lista2 = list()
for x in range(10):
    if lista[x] > 5 :
        lista2.append(lista[x])
print(lista2)
for y in range(5):
    lista.remove(lista2[y])
print(lista)
lista = lista + lista2
print(lista)
lista3 = list()
#Zadanie7
lista.insert(0, 0)
print(lista)
lista3 = lista
lista3.sort(reverse = True)
print(lista3)
#Zadanie8
student = ("Sebastian Krzynówek", "Marcin Kozłowski")
nr_indeksu = (151048, 151049)
print(f'{student[0]} o numerze indeksu {nr_indeksu[0]} oraz {student[1]} o numerze indeksu {nr_indeksu[1]}')
#Zadanie9
slownik = {'imie_nazwisko': 'Sebastian Krzynówek', 'nr_indexu': 151048, 'wiek': 20, 'adres_email': 'sebakrzynek@gmail.com', 'rok_ur' : 2000, 'adres' : 'Dobry Las 166'}
print(slownik['imie_nazwisko'])
print(slownik['adres'])
#Zadanie10
lista_tel = (518362447, 500100200, 518362447, 500900200, 200400500,111222333, 111222333)
telefony = set(lista_tel)
print(telefony)
#Zadanie11
elem = list(range(1, 11, 1))
print(elem)
#Zadanie12
elem2 = list(range(100, -21, -5))
print(elem2)
#Zadanie13
kierowca1 = {'imie': 'Sebastian', 'nazwisko': 'Krzynówek', 'rok_ur': '2000', 'prawo_jazdy': 'kat.B'}
auto1 = {'marka': 'Volvo', 'model': 'C30', 'silnik': '1.6 D2', 'moc_silnika': '114KM'}
lista_slow = [kierowca1, auto1]
print("Kierowca " + lista_slow[0].get('imie') + " " + lista_slow[0].get('nazwisko') + " rocznik " + lista_slow[0].get('rok_ur') + " mający prawo jazdy " + lista_slow[0].get('prawo_jazdy') + " jechał samochodem " + lista_slow[1].get('marka') + " " + lista_slow[1].get('model') + " wersją z silnikiem " + lista_slow[1].get('silnik') + " o mocy " + lista_slow[1].get('moc_silnika'))


