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

