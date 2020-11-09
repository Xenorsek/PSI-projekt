#ZAD 1 i 2
zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Marcin"
nazwisko = "Kozlowski"
liczba1 = zmienna.count(imie[2])
liczba2 = zmienna.count(nazwisko[3])
print(f"W tekście jest {liczba1} {imie[2]} liter oraz {liczba2} liter {nazwisko[3]}")
#ZAD4
ciag = "bedzie ciekawie"
print(dir(ciag))
help(ciag.expandtabs())
"""
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.
"""
#zad 5
print(imie[::-1]+" "+nazwisko[::-1])
#zad 6
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
lista = [0,*lista,*lista2]
print(lista)
lista3 = lista
lista3.sort(reverse=True)
print(lista3)
#zad 8
student1 = "marcin","nazwiskoj",4874672
student2 = "aligner","nazwisko", 4847393
#zad 9
slownik = dict([
    (48746,["marcin","abc",1829,"dskdsk@interia.pl","tez ma adres"]),
    (48473,["aligner","dcb",1999,"dkasdk@wp.pl","adres ma"])
])
print(slownik[48473])
#zad 10
listatel = [5,5,5,5,4,34,3,5,34,534,5345,346,35324,42,4,54]
print(listatel)
telefony=set(listatel)
print(telefony)
#zad 11
x = range(1, 10)
for n in x:
  print(n)
#zad 12
x = range(100, 20, -5)
for n in x:
  print(n)
#zad 13
slownika = {
  "brand": "Ford",
  "model": "Mustang",
  "rok": "1964"
}
slownikb = {
    "imie":"albert",
    "nazwisko":"karbin",
    "indeks":"484833"
}
lista = [slownika,slownikb]
print("student "+lista[1].get("imie")+" " +lista[1].get("nazwisko")+" z indeksem numer "+lista[1].get("indeks")+ " jechal swoim "+lista[0].get("model") +" "+lista[0].get("brand")+" z roku "+lista[0].get("rok"))