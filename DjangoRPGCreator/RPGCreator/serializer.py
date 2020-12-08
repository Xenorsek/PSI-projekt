from rest_framework import serializers
from RPGCreator.models import Postac, Statystyki, Ewkipunek, Bestiariusz, SpecjalneAtaki, Typ

class PostacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postac
        fields = ['idPostac', 'Nazwa', 'Rasa', 'Poziom', 'Profesja']

class StatystykiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statystyki
        fields = ['idStatystyki', 'Postac_idPostac', 'Inteligencja', 'Sila', 'Zywotnosc', 'Zwinnosc', 'PktZdrowia']

class EkwipunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ewkipunek
        fields = ['idEwkipunek', 'Nazwa']

class BestiariuszSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bestiariusz
        fields = ['idBestiariusz', 'Typ_idTyp', 'Nazwa', 'HP', 'Poziom', 'SpecjalneAtaki', 'OpisBestii', 'Ekwipunek_idEkwipunek']

class SpecjalneAtakiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecjalneAtaki
        fields = ['idSpecjalneAtaki', 'Nazwa', 'Obrazenia', 'Efekt', 'Opis']

class TypSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typ
        fields = ['idTyp', 'Nazwa', 'Odpornosc', 'OpisTypu']