from django.urls import path
from .views import indexPageView, aboutPageView, drugDetailsPageView, presDetailsPageView

urlpatterns = [
    path('drug/<str:name>/', drugDetailsPageView, name = 'drug'),
    path('prescriber/<int:id>/', presDetailsPageView, name = 'prescriber'),
    path('about/', aboutPageView, name = 'about'),
    path('', indexPageView, name = 'index'),
]
