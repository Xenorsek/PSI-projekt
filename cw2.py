#Zadanie 1
def funkcja1(a_lista, b_lista):
    c_lista = list()
    for i in range(len(a_lista)):
        if a_lista[i] % 2 == 0:
            c_lista.append(a_lista[i])
    for j in range(len(b_lista)):
        if b_lista[j] % 2 == 1:
            c_lista.append(b_lista[j])

    return c_lista


print(funkcja1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


#Zadanie2
def funkcja2(data_text):
    slownik = {}
    lista = list(data_text)
    slownik = dict([("length", len(data_text)), ("letters", lista), ("big_letters", data_text.upper()), ("small_letters", data_text.lower())])
    return slownik

print(funkcja2("Legia to stary kurczak"))

#Zadanie3
def listToString(lista):
    str = ""

    for x in lista:
        str += x

    return str

def funkcja3(text, letter):
    listaa = list(text)
    while listaa.count(letter) != 0:
            listaa.remove(letter)
    return listToString(listaa)

print(funkcja3("Legia Warszawa", "s"))

#Zadanie4
def funkcja4(temperature_type):
    a = input("Na jakie stopnie przeliczyć temperaturę? 1-Fahrenheit, 2- Rankine, 3-Kelvin  ")
    a = int(a)
    if a == 1:
        temperature_type = temperature_type * (9/5 + 32)
        print(temperature_type)
    elif a == 2:
        temperature_type = (temperature_type + 273.15) * 9/5
        print(temperature_type)
    else :
        temperature_type = temperature_type + 273.15
        print(temperature_type)

funkcja4(15)

#Zadanie5
class Calculator:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

dzialanie = Calculator(5, 6)

print(dzialanie.add())
print(dzialanie.difference())
print(dzialanie.multiply())
print(dzialanie.divide())

#Zadanie6
class ScenceCalculator(Calculator):
    def exponentiation(self):
        return pow(self.a, self.b)

potegowanie = ScenceCalculator(2, 1)
print(potegowanie.exponentiation())

#Zadanie7
def funkcja5(text):
    print(f'{text[::-1]}')

funkcja5("koteł")

#Zadanie9
import file_menager as menagoplikow

k = menagoplikow.FileMenager("notatka.txt")

k.read_file("notatka.txt")
k.update_file("Zabrze")










