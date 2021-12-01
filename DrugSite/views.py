from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'DrugSite/index.html')

def aboutPageView(request):
    return render(request, 'DrugSite/about.html')