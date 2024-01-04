from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# The next step is to point the root URLconf at the polls.urls module.
