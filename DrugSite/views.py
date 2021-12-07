from django.shortcuts import render
from DrugSite.models import Drug, Prescriber, StateData, Triple
from django.db.models import Q, F
from tkinter import messagebox

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
        if request.POST['searched']:
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
                    'prescribers': pres,
                    'total': len(pres)

                }
                return render(request, 'DrugSite/results_pres.html', context)
        else:
            searched = 'All Prescribers'
            pres = Prescriber.objects.all().order_by('lname')

            context = {
                'searched': searched,
                'prescribers': pres,
                'total': len(pres)
            }
            return render(request, 'DrugSite/results_pres.html', context)
    else:
        return render(request, 'DrugSite/results_pres.html')

def filterResultsPageView(request, searched):
    try:
        isopioid = request.POST['isopioid']
        if searched == 'All Drugs':
            drugs = Drug.objects.filter(isopioid =isopioid)
        else:
            drugs = Drug.objects.filter(drugname__contains=searched.replace(' ','.').upper(), isopioid=isopioid)
        
        for drug in drugs:
            drug.drugname = drug.drugname.replace('.',' ').lower()

        context = {
            'searched': searched,
            'drugs': drugs,
            'total': len(drugs)
        }
        return render(request, 'DrugSite/results_drug.html', context)
    except Exception:
        if searched == 'All Prescribers':
            pres = Prescriber.objects.all().order_by('lname')
        else:
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
            'prescribers': pres,
            'total': len(pres)
        }
        return render(request, 'DrugSite/results_pres.html', context)

def resultsDrugPageView(request):
    if request.method == 'POST':
        if request.POST['searched']:
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
                    'drugs': drugs,
                    'total': len(drugs)

                }
                return render(request, 'DrugSite/results_drug.html', context)
        else:
            searched = 'All Drugs'
            drugs = Drug.objects.all().order_by('drugname')

            for drug in drugs:
                drug.drugname = drug.drugname.replace('.',' ').lower()

            context = {
                'searched': searched,
                'drugs': drugs,
                'total': len(drugs)
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

    return searchPageView(request)

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

def statsPageView(request):
    topPresOpioid = Prescriber.objects.raw('''SELECT npi, concat(fname, ' ', lname) as fullname, t1.qty
                                        From pd_prescriber p
                                        Inner Join (Select t.prescriberid, sum(qty) as qty
	                                        From pd_triple t
	                                        Inner Join pd_drugs d on d.drugname = t.drugname
	                                        Where d.isopioid = 'True'
	                                        Group by t.prescriberid) t1 on t1.prescriberid = p.npi
                                        Order by t1.qty desc''')

    topDrug = Drug.objects.raw('''SELECT drugid, d.drugname, sum(qty) as qty
                                From pd_drugs d
                                Inner join pd_triple t on t.drugname = d.drugname
                                Group by drugid, d.drugname
                                Order by qty desc''')
    for drug in topDrug:
        drug.drugname = drug.drugname.replace('.',' ').lower()

    topOpioid = Drug.objects.raw('''SELECT drugid, t1.drugname, t1.qty
                                    From pd_drugs d
                                    Inner Join (Select t.drugname, sum(qty) as qty
	                                    From pd_triple t
	                                    Inner Join pd_drugs d on d.drugname = t.drugname
	                                    Where isopioid = 'True'
	                                    Group by t.drugname) t1 on t1.drugname = d.drugname
                                    Order by t1.qty desc''')
    for drug in topOpioid:
        drug.drugname = drug.drugname.replace('.',' ').lower()
        print(drug.drugname)

    topPres = Prescriber.objects.all().order_by('-totalprescriptions')

    states = StateData.objects.raw('''SELECT stateabbrev, state, population, deaths, round(deaths/(population/100000)::numeric,1) as dpp
                                    From pd_statedata
                                    Order by DPP Desc''')

    context = {
        "topDrug": topDrug,
        "topPresOpioid": topPresOpioid,
        "topOpioid": topOpioid,
        "topPres": topPres,
        "states": states,
    }
    return render(request, 'Drugsite/stats.html', context)

def statePageView(request, ab):
    states = StateData.objects.raw(f'''SELECT stateabbrev, state, population, deaths, dpp, rank
                                        From (SELECT stateabbrev, state, population, deaths, DPP, RANK () OVER ( 
		                                    ORDER BY DPP Desc
	                                        ) rank
                                                From (Select stateabbrev, state, population, deaths, round(deaths/(population/100000)::numeric,1) as DPP
	                                        From pd_statedata) t1) t2
                                        Where stateabbrev = '{ab}'
                                    ''')
    pres = Prescriber.objects.filter(state=ab).order_by('-totalprescriptions')

    for state in states:
        context = {
            "state": state,
            "prescribers": pres
        }
    return render(request, 'DrugSite/state.html', context)

def statesPageView(request):
    states = StateData.objects.all().order_by('state')

    context = {
        "states": states
    }
    return render(request, 'DrugSite/states.html', context)

