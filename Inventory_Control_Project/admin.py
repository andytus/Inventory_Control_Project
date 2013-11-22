from django.contrib import admin
from Inventory_Control_Project.models import Inventory, Employee, Type
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
  list_display = ('type', 'description', 'serialnumber', 'signedoutby', 'toolkitnumber')
  list_filter = ('datesignedout', 'toolkitnumber', 'description', 'type','signedoutby')
  search_fields =  ['serialnumber', 'description', 'type__invtype']
  list_editable = ('signedoutby', 'toolkitnumber')
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Employee)
admin.site.register(Type)