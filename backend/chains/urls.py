from django.urls import path

from .views import chain, index, prompt

urlpatterns = [
    path('', index, name='index'),
    path('prompt/', prompt, name='prompt'),
    path('chain/', chain, name='chain'),
]
