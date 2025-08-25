from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_view, name='post_view'),  # agora a raiz de /blog/ chama post_view
]
