from django.db import models

# Create your models here.
class Drug(models.Model):
    drugname = models.CharField(max_length=30, verbose_name="Drug Name")
    isopiod = models.BooleanField(default=False, verbose_name="Is Opioid?")

    class Meta:
        db_table = "pd_drugs"

    def __str__(self):
        return (self.drugname)

class Prescriber(models.Model):
    fname = models.CharField(max_length=11, verbose_name="First Name")
    lname = models.CharField(max_length=11, verbose_name="Last Name")
    gender = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    credentials = models.CharField(max_length=20)
    specialty = models.CharField(max_length=62)
    levemir = models.IntegerField(default=0)
    levemirflexpen = models.IntegerField(default=0)
    levetiracetam = models.IntegerField(default=0)
    levofloxacin = models.IntegerField(default=0)
    levothyroxinesodium = models.IntegerField(default=0)
    lithiumcarbonate = models.IntegerField(default=0)
    lorazepam = models.IntegerField(default=0)
    lisinoprilhydrochlorothiazide= models.IntegerField(default=0)
    losartanpotassium = models.IntegerField(default=0)
    lovastatin = models.IntegerField(default=0)
    lovaza = models.IntegerField(default=0)
    lumigan = models.IntegerField(default=0)
    lyrica = models.IntegerField(default=0)
    meclizinehcl = models.IntegerField(default=0)
    meloxicam = models.IntegerField(default=0)
    metforminhcl = models.IntegerField(default=0)
    metforminhcler = models.IntegerField(default=0)
    methadonehcl = models.IntegerField(default=0)
    methocarbamol = models.IntegerField(default=0)
    methotrexate = models.IntegerField(default=0)
    methylprednisolone = models.IntegerField(default=0)
    metoclopramidehcl = models.IntegerField(default=0)
    metolazone= models.IntegerField(default=0)
    metoprololsuccinate = models.IntegerField(default=0)
    metoprololtartrate = models.IntegerField(default=0)
    metronidazole = models.IntegerField(default=0)
    mirtazapine = models.IntegerField(default=0)
    montelukastsodium = models.IntegerField(default=0)
    morphinesulfateer= models.IntegerField(default=0)
    mupirocin = models.IntegerField(default=0)
    mirtazapin = models.IntegerField(default=0)
    nabumetone = models.IntegerField(default=0)
    namenda = models.IntegerField(default=0)
    namendaxr = models.IntegerField(default=0)
    naproxen = models.IntegerField(default=0)
    nasonex = models.IntegerField(default=0)
    nexium = models.IntegerField(default=0)
    niaciner = models.IntegerField(default=0)
    nifedicalxl = models.IntegerField(default=0)
    nifedipineer = models.IntegerField(default=0)
    nitrofurantoinmonomacro = models.IntegerField(default=0)
    nitrostat = models.IntegerField(default=0)
    nortriptylinehcl = models.IntegerField(default=0)
    novolog = models.IntegerField(default=0)
    novologflexpen = models.IntegerField(default=0)
    nystatin = models.IntegerField(default=0)
    olanzapine = models.IntegerField(default=0)
    omeprazole = models.IntegerField(default=0)
    ondansetronhcl = models.IntegerField(default=0)
    ondansetronodt = models.IntegerField(default=0)
    onglyza = models.IntegerField(default=0)
    oxcarbazepine = models.IntegerField(default=0)
    oxybutyninchloride = models.IntegerField(default=0)
    oxybutyninchlorideer = models.IntegerField(default=0)
    oxycodoneacetaminophen = models.IntegerField(default=0)
    oxycodonehcl = models.IntegerField(default=0)
    oxycontin = models.IntegerField(default=0)
    pantoprazolesodium = models.IntegerField(default=0)
    paroxetinehcl = models.IntegerField(default=0)
    phenobarbital = models.IntegerField(default=0)
    phenytoinsodiumextended = models.IntegerField(default=0)
    pioglitazonehcl = models.IntegerField(default=0)
    polyethyleneglycol3350 = models.IntegerField(default=0)
    potassiumchloride = models.IntegerField(default=0)
    pradaxa = models.IntegerField(default=0)
    pramipexoledihydrochloride = models.IntegerField(default=0)
    pravastatinsodium = models.IntegerField(default=0)
    prednisone = models.IntegerField(default=0)
    premarin = models.IntegerField(default=0)
    primidone = models.IntegerField(default=0)
    proairhfa = models.IntegerField(default=0)
    promethazinehcl = models.IntegerField(default=0)
    propranololhcl = models.IntegerField(default=0)
    propranololhcler = models.IntegerField(default=0)
    quetiapinefumarate = models.IntegerField(default=0)
    quinaprilhcl = models.IntegerField(default=0)
    raloxifenehcl = models.IntegerField(default=0)
    ramipril = models.IntegerField(default=0)
    ranexa = models.IntegerField(default=0)
    ranitidinehcl = models.IntegerField(default=0)
    restasis = models.IntegerField(default=0)
    risperidone = models.IntegerField(default=0)
    ropinirolehcl = models.IntegerField(default=0)
    seroquelxr = models.IntegerField(default=0)
    sertralinehcl = models.IntegerField(default=0)
    simvastatin = models.IntegerField(default=0)
    sotalol = models.IntegerField(default=0)
    spiriva = models.IntegerField(default=0)
    spironolactone = models.IntegerField(default=0)
    sucralfate = models.IntegerField(default=0)
    sulfamethoxazoletrimethoprim = models.IntegerField(default=0)
    sumatriptansuccinate = models.IntegerField(default=0)
    symbicort = models.IntegerField(default=0)
    synthroid = models.IntegerField(default=0)
    tamsulosinhcl = models.IntegerField(default=0)
    temazepam = models.IntegerField(default=0)
    terazosinhcl = models.IntegerField(default=0)
    timololmaleate = models.IntegerField(default=0)
    tizanidinehcl = models.IntegerField(default=0)
    tolterodinetartrateer = models.IntegerField(default=0)
    topiramate = models.IntegerField(default=0)
    toprolxl = models.IntegerField(default=0)
    torsemide = models.IntegerField(default=0)
    tramadolhcl = models.IntegerField(default=0)
    travatanz = models.IntegerField(default=0)
    trazodonehcl = models.IntegerField(default=0)
    triamcinoloneacetonide = models.IntegerField(default=0)
    triamterenehydrochlorothiazid = models.IntegerField(default=0)
    valacyclovir = models.IntegerField(default=0)
    valsartan = models.IntegerField(default=0)
    valsartanhydrochlorothiazide = models.IntegerField(default=0)
    venlafaxinehcl = models.IntegerField(default=0)
    venlafaxinehcler = models.IntegerField(default=0)
    ventolinhfa = models.IntegerField(default=0)
    verapamiler = models.IntegerField(default=0)
    vesicare = models.IntegerField(default=0)
    voltaren = models.IntegerField(default=0)
    vytorin = models.IntegerField(default=0)
    warfarinsodium = models.IntegerField(default=0)
    xarelto = models.IntegerField(default=0)
    zetia = models.IntegerField(default=0)
    ziprasidonehcl = models.IntegerField(default=0)
    zolpidemtartrate = models.IntegerField(default=0)
    

    

    




    class Meta:
        db_table = "pd_prescriber"


class StateData(models.Model):
    state = models.CharField(max_length=14)
    stateabbrev = models.CharField(max_length=2)
    population = models.IntegerField(default=0)
    death = models.IntegerField(default=0)

    class Meta:
        db_table = "pd_statedata"

    def __str__(self):
        return (self.state)

class Triple(models.Model):
    prescriberid = models.ForeignKey(Prescriber, default="", verbose_name="PrescriberID", on_delete=models.DO_NOTHING, to_field='prescriberid')
    drugname = models.ForeignKey(Drug, default="", verbose_name="Category", on_delete=models.DO_NOTHING, to_field='drugname')
    qty = models.IntegerField(default=0)

    class Meta:
        db_table = 'pd_triple'

