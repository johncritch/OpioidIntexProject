from django.shortcuts import render
from DrugSite.models import Drug, Prescriber, Triple
from django.db.models import Q

# Create your views here.
def indexPageView(request):
    return render(request, 'DrugSite/index.html')

def aboutPageView(request):
    return render(request, 'DrugSite/about.html')

def searchPageView(request):
    pres = Prescriber.objects.all().order_by('-totalprescriptions')
    drugs = Drug.objects.raw('''SELECT drugid, d.drugname, sum(qty) as qty
                                From pd_drugs d
                                Inner join pd_triple t on t.drugname = d.drugname
                                Group by drugid, d.drugname
                                Order by qty desc''')

    for drug in drugs:
        drug.drugname = drug.drugname.replace('.',' ').lower()

    context = {
        "prescriber": pres,
        "drugs": drugs
    }
    return render(request, 'DrugSite/search.html', context)

def resultsPresPageView(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        try:
            a = searched.split()
            fname,lname = a[0],a[1]
            pres = Prescriber.objects.get(fname=fname, lname = lname)

            return presDetailsPageView(request, id = pres.npi)
        except Exception:
            pres = Prescriber.objects.filter(Q(lname__contains=searched) | Q(fname__contains=searched)).order_by('lname')
            context = {
                'searched': searched,
                'prescribers': pres

            }
            return render(request, 'DrugSite/results_pres.html', context)
    
    else:
        return render(request, 'DrugSite/results_pres.html')

def filterResultsPageView(request, searched):
    pres = Prescriber.objects.filter(Q(lname__contains=searched) | Q(fname__contains=searched)).order_by('lname')
    if request.POST['gender']:
        pres = pres.filter(gender = request.POST['gender'])
    if request.POST['state']:
        pres = pres.filter(state = request.POST['state'])
    if request.POST['credentials']:
        pres = pres.filter(credentials__contains = request.POST['credentials'])
    if request.POST['specialty']:
        pres = pres.filter(specialty__contains = request.POST['specialty'])

    context = {
        'searched': searched,
        'prescribers': pres
    }
    return render(request, 'DrugSite/results_pres.html', context)

def resultsDrugPageView(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        try:
            drug = Drug.objects.get(drugname=searched.replace(' ','.').upper())

            return drugDetailsPageView(request, name=drug.drugname)

        except Exception:
            drugs = Drug.objects.filter(drugname__contains=searched.replace(' ','.').upper()).order_by('drugname')

            for drug in drugs:
                drug.drugname = drug.drugname.replace('.',' ').lower()

            context = {
                'searched': searched,
                'drugs': drugs

            }
            return render(request, 'DrugSite/results_drug.html', context)
    
    else:
        return render(request, 'DrugSite/results_drug.html')

def drugDetailsPageView(request, name):
    drug = Drug.objects.get(drugname = name.replace(' ','.').upper())

    triple = Triple.objects.raw(f'''SELECT * 
                                    From pd_triple t 
                                    INNER JOIN pd_prescriber p On p.npi = t.prescriberid 
                                    Where drugname = '{name.replace(' ','.').upper()}'
                                    ORDER BY t.QTY DESC 
                                    Limit 10''')

    drug.drugname = drug.drugname.replace('.',' ').lower()                              

    context = {
        "drug": drug,
        "prescribers": triple
    }

    return render(request, "DrugSite/drug_details.html", context)

def presDetailsPageView(request, id):
    data = Prescriber.objects.get(npi = id)

    triple = Triple.objects.raw(f'''SELECT id, prescriberid, t.drugname, qty, average
                                    From pd_triple t
                                    Inner Join (Select drugname, round(avg(qty)) as average
	                                    From pd_triple
	                                    Group by drugname) t1 On t1.drugname = t.drugname
                                    Where prescriberid = {id}''')

    for item in triple:
        item.drugname = item.drugname.replace('.',' ').lower()

    context = {
        "pres": data,
        "drugs": triple
    }
    return render(request, 'DrugSite/pres_details.html', context)

def addPrescriberPageView(request):
    if request.method == 'POST':
        pres = Prescriber()

        pres.npi = request.POST['npi']
        pres.fname = request.POST['fname']
        pres.lname = request.POST['lname']
        pres.gender = request.POST['gender']
        pres.state = request.POST['state']
        pres.credentials = request.POST['credentials']
        pres.specialty = request.POST['specialty']
        pres.isopioidprescriber = request.POST['isopioidprescriber']

        pres.save()

        return presDetailsPageView(request, pres.npi)
    else:
        return render(request, 'DrugSite/add_pres.html')

def editPrescriberPageView(request, id):
    data = Prescriber.objects.get(npi = id)

    context = {
        'record': data
    }
    return render(request, 'DrugSite/edit_pres.html', context)

def updatePrescriberPageView(request):
    if request.method == 'POST':
        id = request.POST['npi']

        pres = Prescriber.objects.get(npi=id)

        pres.fname = request.POST['fname']
        pres.lname = request.POST['lname']
        pres.gender = request.POST['gender']
        pres.state = request.POST['state']
        pres.credentials = request.POST['credentials']
        pres.specialty = request.POST['specialty']
        pres.isopioidprescriber = request.POST['isopioidprescriber']

        pres.save()

    return presDetailsPageView(request, pres.npi)

def deletePrescriberPageView(request, id):
    data = Prescriber.objects.get(npi = id)

    data.delete()

    return indexPageView(request)

def addPrescriptionPageView(request, id):
    record = Prescriber.objects.get(npi = id)
    drugs = Drug.objects.all().order_by('drugname')

    for drug in drugs:
        drug.drugname = drug.drugname.replace('.',' ').lower()

    context = {
        "record": record,
        "drugs": drugs
    }
    return render(request, 'DrugSite/add_prescription.html', context)

def updatePrescriptionPageView(request):
    if request.method == 'POST':
        pres = Prescriber.objects.get(npi = request.POST['npi'])
        pres.totalprescriptions += int(request.POST['qty'])
        
        try:
            record = Triple.objects.get(prescriberid = request.POST['npi'], drugname = request.POST['drugname'].upper())
            record.qty += int(request.POST['qty'])

        except Exception:
            maxId = Triple.objects.all().order_by('-id')[0]
            record = Triple()
            record.id = maxId.id + 1
            record.prescriberid = request.POST['npi']
            record.drugname = request.POST['drugname'].upper()
            record.qty = int(request.POST['qty'])

        pres.save()
        record.save()

    return presDetailsPageView(request, record.prescriberid)


