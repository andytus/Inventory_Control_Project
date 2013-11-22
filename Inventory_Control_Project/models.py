from django.db import models

# Create your models here.
class Employee(models.Model):
    employeename = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.employeename


    class Meta:
        verbose_name_plural = "Employees"

class Type(models.Model):
    invtype = models.CharField(max_length=200, )

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.invtype
    class Meta:
        verbose_name_plural = "Types"

class Inventory(models.Model):
    serialnumber = models.CharField(max_length=200, blank=True,)
    type = models.ForeignKey(Type)
    description = models.CharField(max_length=200, blank = True)
    signedoutby = models.ForeignKey(Employee)
    toolkitnumber = models.CharField(max_length=15, blank=True)
    datesignedout = models.DateTimeField('date signed out', auto_now=True)

   # def __unicode__(self):  # Python 3: def __str__(self):
    #  return self.description + " " + self.type.invtype + " " + self.serialnumber + " Signed out by: " + self.signedoutby.employeename


    class Meta:
        verbose_name_plural = "Inventories"





