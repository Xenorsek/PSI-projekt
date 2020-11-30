from rest_framework import serializers

class PostacSerializer(serializers.Serializer):
    idPostac = serializers.IntegerField()
    Nazwa = serializers.CharField(max_length=45)
    Rasa = serializers.CharField(max_length=45)
    Poziom = serializers.IntegerField()
    Profesja = serializers.CharField()
    def create(self, validated_data):
        return PostacSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idPostac = validated_data.get('idPostac', instance.idPostac)
        instance.Nazwa = validated_data.get('Nazwa', instance.Nazwa)
        instance.Rasa = validated_data.get('Rasa', instance.Rasa)
        instance.Poziom = validated_data.get('Poziom', instance.Poziom)
        instance.Profesja = validated_data.get('Profesja', instance.Profesja)
        return instance

class StatystykiSerializer(serializers.Serializer):
    idStatystyki= serializers.IntegerField()
    Postac_idPostac = serializers.IntegerField()
    Inteligencja = serializers.IntegerField(default=10)
    Sila = serializers.IntegerField(default=10)
    Zywotnosc = serializers.IntegerField(default=10)
    Zwinnosc = serializers.IntegerField(default=10)
    PktZdrowia = serializers.IntegerField(default=10)
    def create(self, validated_data):
        return SpecjalneAtakiSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idStatystyki = validated_data.get('idStatystyki', instance.idStatystyki)
        instance.Postac_idPostac= validated_data.get('Postac_idPostac', instance.Postac_idPostac)
        instance.Inteligencja= validated_data.get('Inteligencja', instance.Inteligencja)
        instance.Sila= validated_data.get('Sila', instance.Sila)
        instance.Zywotnosc = validated_data.get('Zywotnosc', instance.Zywotnosc)
        instance.PktZdrowia = validated_data.get('PktZdrowia', instance.PktZdrowia)
        return instance

class EkwipunekSerializer(serializers.Serializer):
    idEkwipunku = serializers.IntegerField()
    Nazwa = serializers.CharField(max_length=45)
    def create(self, validated_data):
        return EkwipunekSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idEkwipunku = validated_data.get('idEkwipunku', instance.idEkwipunku)
        instance.Nazwa= validated_data.get('Nazwa', instance.Nazwa)
        return instance

class BestiariuszSerializer(serializers.Serializer):
    idBestiariusz = serializers.IntegerField()
    Typ_idTyp = serializers.IntegerField()
    Nazwa = serializers.CharField(max_length=45)
    HP = serializers.CharField(max_length=45)
    Poziom = serializers.CharField(max_length=45)
    SpecjalneAtaki = serializers.IntegerField()
    OpisBestii = serializers.CharField(max_length=200)
    Ekwipunek_idEkwipunek = serializers.IntegerField()
    def create(self, validated_data):
        return BestiariuszSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idBestiariusz = validated_data.get('idBestiariusz', instance.idBestiariusz)
        instance.Typ_idTyp = validated_data.get('Typ_idTyp', instance.Typ_idTyp)
        instance.Nazwa = validated_data.get('Nazwa', instance.Nazwa)
        instance.HP = validated_data.get('HP', instance.HP)
        instance.Poziom = validated_data.get('Poziom', instance.Poziom)
        instance.SpecjalneAtaki = validated_data.get('SpecjalneAtaki', instance.SpecjalneAtaki)
        instance.OpisBestii = validated_data.get('OpisBestii', instance.OpisBestii)
        instance.Ekwipunek_idEkwipunek = validated_data.get('Ekwipunek_idEkwipunek', instance.Ekwipunek_idEkwipunek)
        return instance


class SpecjalneAtakiSerializer(serializers.Serializer):
    idSpecjalneAtaki = serializers.IntegerField()
    Nazwa = serializers.CharField(max_length=45)
    Obrazenia = serializers.IntegerField()
    Efekt = serializers.CharField(default='brak')
    Opis = serializers.TextField()
    def create(self, validated_data):
        return SpecjalneAtakiSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idSpecjalneAtaki = validated_data.get('idSpecjalneAtaki', instance.idSpecjalneAtaki)
        instance.Nazwa = validated_data.get('Nazwa', instance.Nazwa)
        instance.Obrazenia = validated_data.get('Obrazenia', instance.Obrazenia)
        instance.Efekt = validated_data.get('Efekt', instance.Efekt)
        instance.Opis = validated_data.get('Opis', instance.Opis)
        return instance

class TypSerializer(serializers.Serializer):
    idTyp = serializers.IntegerField()
    Nazwa = serializers.CharField(max_length=45)
    Odpornosc = serializers.CharField(default='brak')
    OpisTypu = serializers.CharField(max_length=45)

    def create(self, validated_data):
        return TypSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.idTyp = validated_data.get('idTyp', instance.idTyp)
        instance.Nazwa = validated_data.get('Nazwa', instance.Nazwa)
        instance.Odpornosc = validated_data.get('Odpornosc', instance.Odpornosc)
        instance.OpisTypu = validated_data.get('OpisTypu', instance.OpisTypu)
        return instance
