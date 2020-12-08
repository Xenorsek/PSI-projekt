from django.db import models

# Create your models here.

class Postac(models.Model):
    idPostac = models.IntegerField()
    Nazwa = models.CharField(max_length=45)
    Rasa = models.CharField(max_length=45)
    Poziom = models.IntegerField()

    RYCERZ = 'RY'
    MAG = 'MA'
    LUCZNIK = 'LU'
    SKRYTOBOJCA = 'SK'

    Postac_wybor = (
        (RYCERZ, 'Rycerz'),
        (MAG, 'Mag'),
        (LUCZNIK, 'Łucznik'),
        (SKRYTOBOJCA, 'Skrytobójca'),
    )
    Profesja = models.CharField(
        max_length=2,
        choices=Postac_wybor,
    )

class Statystyki(models.Model):
    idStatystyki = models.IntegerField()
    Postac_idPostac = models.IntegerField()
    Inteligencja = models.IntegerField(
        default=10,
    )
    Sila= models.IntegerField(
        default=10,
    )
    Zywotnosc = models.IntegerField(
        default=10,
    )
    Zwinnosc = models.IntegerField(
        default=10,
    )
    PktZdrowia = models.IntegerField(
        default=50,
    )

class Ewkipunek(models.Model):
    idEwkipunek = models.IntegerField()
    Nazwa = models.CharField(max_length=45)

class Bestiariusz(models.Model):
    idBestiariusz = models.IntegerField()
    Typ_idTyp = models.IntegerField()
    Nazwa = models.CharField(max_length=45)
    HP = models.CharField(max_length=45)
    Poziom = models.CharField(max_length=45)
    SpecjalneAtaki = models.IntegerField()
    OpisBestii = models.CharField(max_length=200)
    Ekwipunek_idEkwipunek = models.IntegerField()

class SpecjalneAtaki(models.Model):
    idSpecjalneAtaki = models.IntegerField()
    Nazwa = models.CharField(max_length=45)
    Obrazenia = models.IntegerField()
    OTRUCIE = 'OT'
    PODPALENIE = 'PO'
    OSLEPIENIE = 'OS'
    SPOWOLNIENIE = 'SP'
    OSLABIENIE = 'OL'
    OGLUSZENIE = 'OG'

    SpecAtak_wybor = (
        (OTRUCIE, 'Otrucie'),
        (PODPALENIE, 'Podpalenie'),
        (OSLEPIENIE, 'Oślepienie'),
        (SPOWOLNIENIE, 'Spowolnienie'),
        (OSLABIENIE, 'Osłabienie'),
        (OGLUSZENIE, 'Ogłuszenie'),
    )
    Efekt = models.CharField(
        max_length=2,
        choices=SpecAtak_wybor,
        default='brak',
    )
    Opis = models.TextField()

class Typ(models.Model):
    idTyp = models.IntegerField()
    Nazwa = models.CharField(max_length=300)
    OTRUCIE = 'OT'
    PODPALENIE = 'PO'
    OSLEPIENIE = 'OS'
    SPOWOLNIENIE = 'SP'
    OSLABIENIE = 'OL'
    OGLUSZENIE = 'OG'

    Odpornosc_wybor = (
        (OTRUCIE, 'Otrucie'),
        (PODPALENIE, 'Podpalenie'),
        (OSLEPIENIE, 'Oślepienie'),
        (SPOWOLNIENIE, 'Spowolnienie'),
        (OSLABIENIE, 'Osłabienie'),
        (OGLUSZENIE, 'Ogłuszenie'),
    )
    Odpornosc = models.CharField(
        max_length=2,
        choices=Odpornosc_wybor,
        default='brak',
    )
    OpisTypu = models.CharField(max_length=300)





