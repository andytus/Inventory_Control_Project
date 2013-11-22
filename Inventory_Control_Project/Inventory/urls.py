from django.conf.urls import patterns, url
from Inventory_Control_Project.Inventory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add'),
    # ex: /polls/5/results/
    url(r'^newemployee/', views.newemployee, name='newEmployee'),
    # ex: /polls/5/vote/
    url(r'^newtype/', views.newtype, name='newtype'),
)