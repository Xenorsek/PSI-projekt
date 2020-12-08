from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from RPGCreator.serializer import *
from RPGCreator.models import *
from django.http import HttpResponse
class PostacList(generics.ListCreateAPIView):
    queryset = Postac.objects.all()
    serializer_class = PostacSerializer

class PostacDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postac.objects.all()
    serializer_class = PostacSerializer

class BestiariuszList(generics.ListCreateAPIView):
    queryset = Bestiariusz.objects.all()
    serializer_class = BestiariuszSerializer

class BestiariuszDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bestiariusz.objects.all()
    serializer_class = BestiariuszSerializer

class EkwipunekList(generics.ListCreateAPIView):
    queryset = Ewkipunek.objects.all()
    serializer_class = EkwipunekSerializer

class EkwipunekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ewkipunek.objects.all()
    serializer_class = EkwipunekSerializer

class StatystykiList(generics.ListCreateAPIView):
    queryset = Statystyki.objects.all()
    serializer_class = StatystykiSerializer

class StatystykiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statystyki.objects.all()
    serializer_class = StatystykiSerializer

class SpecjalneAtakiList(generics.ListCreateAPIView):
    queryset = SpecjalneAtaki.objects.all()
    serializer_class = SpecjalneAtakiSerializer

class SpecjalneAtakiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecjalneAtaki.objects.all()
    serializer_class = StatystykiSerializer

class TypList(generics.ListCreateAPIView):
    queryset = Typ.objects.all()
    serializer_class = TypSerializer

class TypDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Typ.objects.all()
    serializer_class = TypSerializer