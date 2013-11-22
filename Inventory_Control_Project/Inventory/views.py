from django.shortcuts import render
from django.http import HttpResponse
from Inventory_Control_Project.models import Inventory, Employee, Type

# Create your views here.


def index(request):
  #  t= Type.objects.all()
   # e
    inventory_list = Inventory.objects.order_by('pk')
    output = ', '.join([str(i.pk) for i in inventory_list])
    return HttpResponse(output)
def add(request):
    return HttpResponse("Placeholder to add inventory to the site.")

def newemployee(request):
    return HttpResponse("You're looking the New Employee Screen.")

def newtype(request):
    return HttpResponse("You're looking at the New Type of Inventory placeholder")