from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^roughs/(?P<pk>\d+)/update/',
        views.roughsUpdate, name="roughs_update"),
    url(r'^roughs/(?P<pk>\d+)/edit/',
        views.roughsEdit, name="roughs_edit"),
    url(r'^roughs/(?P<pk>\d+)/',
        views.roughsDetail, name="roughs_detail"),
    url(r'^roughs/create/', views.roughsCreate, name="roughs_create"),
    url(r'^roughs/new/', views.roughsNew, name="roughs_new"),
    url(r'^roughs/', views.roughsIndex, name="roughs_index"),
    
    url(r'^fairways/(?P<pk>\d+)/update/',
        views.fairwaysUpdate, name="fairways_update"),
    url(r'^fairways/(?P<pk>\d+)/edit/',
        views.fairwaysEdit, name="fairways_edit"),
    url(r'^fairways/(?P<pk>\d+)/',
        views.fairwaysDetail, name="fairways_detail"),
    url(r'^fairways/create/', views.fairwaysCreate, name="fairways_create"),
    url(r'^fairways/new/', views.fairwaysNew, name="fairways_new"),
    url(r'^fairways/', views.fairwaysIndex, name="fairways_index"),

    url(r'^tees/(?P<pk>\d+)/update/',
        views.teesUpdate, name="tees_update"),
    url(r'^tees/(?P<pk>\d+)/edit/',
        views.teesEdit, name="tees_edit"),
    url(r'^tees/(?P<pk>\d+)/',
        views.teesDetail, name="tees_detail"),
    url(r'^tees/create/', views.teesCreate, name="tees_create"),
    url(r'^tees/new/', views.teesNew, name="tees_new"),
    url(r'^tees/', views.teesIndex, name="tees_index"),
    
    url(r'^greens/(?P<pk>\d+)/update/',
        views.greensUpdate, name="greens_update"),
    url(r'^greens/(?P<pk>\d+)/edit/',
        views.greensEdit, name="greens_edit"),
    url(r'^greens/(?P<pk>\d+)/',
        views.greensDetail, name="greens_detail"),
    url(r'^greens/create/', views.greensCreate, name="greens_create"),
    url(r'^greens/new/', views.greensNew, name="greens_new"),
    url(r'^greens/', views.greensIndex, name="greens_index"),
    
    url(r'^fertilizers/(?P<pk>\d+)/update/',
        views.fertUpdate, name="fert_update"),
    url(r'^fertilizers/(?P<pk>\d+)/edit/',
        views.fertEdit, name="fert_edit"),
    url(r'^fertilizers/(?P<pk>\d+)/', 
        views.fertDetail, name="fert_detail"),
    url(r'^fertilizers/create/', views.createFert, name="create_fert"),
    url(r'^fertilizers/new/', views.newFert, name="new_fert"),
    url(r'^fertilizers/', views.fertIndex, name="fert_index"),
    
    url(r'^', views.index, name="index"),
]
