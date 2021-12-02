from django.shortcuts import render
from DrugSite.models import Drug, Prescriber, Triple

# Create your views here.
def indexPageView(request):
    return render(request, 'DrugSite/index.html')

def aboutPageView(request):
    return render(request, 'DrugSite/about.html')

def drugDetailsPageView(request, name):
    data = Drug.objects.get(drugname = name.upper())
    triple = Triple.objects.filter(drugname = name.upper())
    prescriber = []

    for item in triple:
        id = item.presciberid
        print(name)
        pres = Prescriber.objects.get(npi = id)
        prescriber.append(pres)

    context = {
        "drug": data,
        "prescriber": prescriber
    }
    print(prescriber)
    return render(request, "DrugSite/drug_details.html", context)

def presDetailsPageView(request, id):
    data = Prescriber.objects.get(npi = id)

    context = {
        "pres": data
    }
    return render(request, 'DrugSite/pres_details.html', context)