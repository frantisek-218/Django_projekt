from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kluby/', views.KlubListView.as_view(), name='klub_list'),
    path('klub/<int:pk>', views.KlubDetailView.as_view(), name='klub_detail'),


    #path('vedouci/<int:pk>', views.KnihaListView.as_view(), name='books_list'),
]
