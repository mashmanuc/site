from django.urls import path
from .import views 
urlpatterns = [
    path('',views.base_hom, name='base_hom'),
    # path('about', views.about, name='about'),
    # path('lusa', views.lusa, name='lusa'),
]
