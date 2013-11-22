from django.conf.urls import patterns, include, url
from django.contrib import admin
from Inventory_Control_Project import Inventory
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Inventory_Control_Project.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inventory/', include('Inventory_Control_Project.Inventory.urls')),
    url(r'^Inventory/', include('Inventory_Control_Project.Inventory.urls'))
)


