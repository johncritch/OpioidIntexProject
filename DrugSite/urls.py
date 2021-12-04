from django.urls import path
from .views import indexPageView, aboutPageView, drugDetailsPageView, presDetailsPageView, addPrescriberPageView, searchPageView, resultsPresPageView
from .views import editPrescriberPageView, updatePrescriberPageView, deletePrescriberPageView, addPrescriptionPageView, updatePrescriptionPageView
from .views import filterResultsPageView, resultsDrugPageView

urlpatterns = [
    path('drug/<str:name>/', drugDetailsPageView, name = 'drug'),
    path('prescriber/<int:id>/', presDetailsPageView, name = 'prescriber'),
    path('about/', aboutPageView, name = 'about'),
    path('addPrescriber/', addPrescriberPageView, name = 'addPres'),
    path('editPrescriber/<int:id>/', editPrescriberPageView, name = 'editPres'),
    path('updatePrescriber/', updatePrescriberPageView, name='updatePres'),
    path('deletePrescriber/<int:id>/', deletePrescriberPageView, name='deletePres'),
    path('addPerscription/<int:id>/', addPrescriptionPageView, name='addPrescription'),
    path('updatePrescription/', updatePrescriptionPageView, name='updatePrescription'),
    path('search/', searchPageView, name='search'),
    path('resultsPrescribers/', resultsPresPageView, name='resultsPres'),
    path('resultsDrugs/', resultsDrugPageView, name='resultsDrug'),
    path('resultsPrescribers/<str:searched>/filtered/', filterResultsPageView, name='filterResults'),
    path('', indexPageView, name = 'index'),
]
