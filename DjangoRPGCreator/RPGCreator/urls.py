from django.urls import path
from . import views

urlpatterns = [
    path('postacie', views.PostacList.as_view()),
    path('postacie/<int:pk>', views.PostacDetail.as_view()),
    path('bestiariusz', views.BestiariuszList.as_view()),
    path('bestiariusz/<int:pk>', views.BestiariuszDetail.as_view()),
    path('ekwipunek', views.EkwipunekList.as_view()),
    path('ekwipunek/<int:pk>', views.EkwipunekDetail.as_view()),
    path('statystyki', views.StatystykiList.as_view()),
    path('statystyki/<int:pk>', views.StatystykiDetail.as_view()),
    path('specjalne', views.SpecjalneAtakiList.as_view()),
    path('specjalne/<int:pk>', views.SpecjalneAtakiDetail.as_view()),
    path('typ', views.TypList.as_view()),
    path('typ/<int:pk>', views.TypDetail.as_view())
]
