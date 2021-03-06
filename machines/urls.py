from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^hours/(?P<pk>\d+)/', views.hourReading, name="hour_read"),
    
    url(r'^spreader/(?P<pk>\d+)/update/', views.spreaderUpdate,
        name="spreader_update"),
    url(r'^spreader/(?P<pk>\d+)/edit/', views.spreaderEdit,
        name="spreader_edit"),
    url(r'^spreader/(?P<pk>\d+)/', views.spreaderDetail,
        name="spreader_detail"),
    url(r'^spreader/create/', views.spreaderCreate,
        name="spreader_create"),
    url(r'^spreader/new/', views.spreaderNew, name="spreader_new"),
    url(r'^spreader/', views.spreaderIndex, name="spreader_index"),
    
    url(r'^tractor/(?P<pk>\d+)/update/', views.tractorUpdate,
        name="tractor_update"),
    url(r'^tractor/(?P<pk>\d+)/edit/', views.tractorEdit,
        name="tractor_edit"),
    url(r'^tractor/(?P<pk>\d+)/', views.tractorDetail,
        name="tractor_detail"),
    url(r'^tractor/create/', views.tractorCreate,
        name="tractor_create"),
    url(r'^tractor/new/', views.tractorNew, name="tractor_new"),
    url(r'^tractor/', views.tractorIndex, name="tractor_index"),
    
    url(r'^util/(?P<pk>\d+)/update/', views.utilUpdate,
        name="util_update"),
    url(r'^util/(?P<pk>\d+)/edit/', views.utilEdit, name="util_edit"),
    url(r'^util/(?P<pk>\d+)/', views.utilDetail, name="util_detail"),
    url(r'^util/create/', views.utilCreate, name="util_create"),
    url(r'^util/new/', views.utilNew, name="util_new"),
    url(r'^util/', views.utilIndex, name="util_index"),
    
    url(r'^rake/(?P<pk>\d+)/update/', views.rakeUpdate,
        name="rake_update"),
    url(r'^rake/(?P<pk>\d+)/edit/', views.rakeEdit, name="rake_edit"),
    url(r'^rake/(?P<pk>\d+)/', views.rakeDetail, name="rake_detail"),
    url(r'^rake/create/', views.rakeCreate, name="rake_create"),
    url(r'^rake/new/', views.rakeNew, name="rake_new"),
    url(r'^rake/', views.rakeIndex, name="rake_index"),
    
    url(r'^cart/(?P<pk>\d+)/update/', views.cartUpdate,
        name="cart_update"),
    url(r'^cart/(?P<pk>\d+)/edit/', views.cartEdit,
        name="cart_edit"),
    url(r'^cart/(?P<pk>\d+)/', views.cartDetail, name="cart_detail"),
    url(r'^cart/create/', views.cartCreate, name="cart_create"),
    url(r'^cart/new/', views.cartNew, name="cart_new"),
    url(r'^cart/', views.cartIndex, name="cart_index"),
    
    url(r'^sprayer/(?P<pk>\d+)/update/', views.sprayerUpdate,
        name="sprayer_update"),
    url(r'^sprayer/(?P<pk>\d+)/edit/', views.sprayerEdit,
        name="sprayer_edit"),
    url(r'^sprayer/(?P<pk>\d+)/', views.sprayerDetail,
        name="sprayer_detail"),
    url(r'^sprayer/create/', views.sprayerCreate, 
        name="sprayer_create"),
    url(r'^sprayer/new/', views.sprayerNew, name="sprayer_new"),
    url(r'^sprayer/', views.sprayerIndex, name="sprayer_index"),
    
    url(r'^aerator/(?P<pk>\d+)/update/', views.aeratorUpdate,
        name="aerator_update"),
    url(r'^aerator/(?P<pk>\d+)/edit/', views.aeratorEdit,
        name="aerator_edit"),
    url(r'^aerator/(?P<pk>\d+)/', views.aeratorDetail,
        name="aerator_detail"),
    url(r'^aerator/create/', views.aeratorCreate, 
        name="aerator_create"),
    url(r'^aerator/new/', views.aeratorNew, name="aerator_new"),
    url(r'^aerator/', views.aeratorIndex, name="aerator_index"),
    
    url(r'^roller/(?P<pk>\d+)/update/', views.rollerUpdate,
        name="roller_update"),
    url(r'^roller/(?P<pk>\d+)/edit/', views.rollerEdit,
        name="roller_edit"),
    url(r'^roller/(?P<pk>\d+)/', views.rollerDetail,
        name="roller_detail"),
    url(r'^roller/create/', views.rollerCreate, name="roller_create"),
    url(r'^roller/new/', views.rollerNew, name="roller_new"),
    url(r'^roller/', views.rollerIndex, name="roller_index"),
    
    url(r'^mower/(?P<pk>\d+)/', views.getMower, 
        name="get_mower"),
    
    url(r'^roughmow/(?P<pk>\d+)/update/', views.roughmowUpdate,
        name="roughmow_update"),
    url(r'^roughmow/(?P<pk>\d+)/edit/', views.roughmowEdit,
        name="roughmow_edit"),
    url(r'^roughmow/(?P<pk>\d+)/', views.roughmowDetail,
        name="roughmow_detail"),
    url(r'^roughmow/create/', views.roughmowCreate,
        name="roughmow_create"),
    url(r'^roughmow/new/', views.roughmowNew, name="roughmow_new"),
    url(r'^roughmow/', views.roughmowIndex, name="roughmow_index"),
    
    url(r'^fairwaymow/(?P<pk>\d+)/update/', views.fairwaymowUpdate,
        name="fairwaymow_update"),
    url(r'^fairwaymow/(?P<pk>\d+)/edit/', views.fairwaymowEdit,
        name="fairwaymow_edit"),
    url(r'^fairwaymow/(?P<pk>\d+)/', views.fairwaymowDetail,
        name="fairwaymow_detail"),
    url(r'^fairwaymow/create/', views.fairwaymowCreate,
        name="fairwaymow_create"),
    url(r'^fairwaymow/new/', views.fairwaymowNew,
        name="fairwaymow_new"),
    url(r'^fairwaymow/', views.fairwaymowIndex,
        name="fairwaymow_index"),
    
    url(r'^teemow/(?P<pk>\d+)/update/', views.teemowUpdate,
        name="teemow_update"),
    url(r'^teemow/(?P<pk>\d+)/edit/', views.teemowEdit,
        name="teemow_edit"),
    url(r'^teemow/(?P<pk>\d+)/', views.teemowDetail,
        name="teemow_detail"),
    url(r'^teemow/create/', views.teemowCreate,
        name="teemow_create"),
    url(r'^teemow/new/', views.teemowNew, name="teemow_new"),
    url(r'^teemow/', views.teemowIndex, name="teemow_index"),
    
    url(r'^greensmow/(?P<pk>\d+)/update/', views.greensmowUpdate,
        name="greensmow_update"),
    url(r'^greensmow/(?P<pk>\d+)/edit/', views.greensmowEdit,
        name="greensmow_edit"),
    url(r'^greensmow/(?P<pk>\d+)/', views.greensmowDetail,
        name="greensmow_detail"),
    url(r'^greensmow/create/', views.greensmowCreate,
        name="greensmow_create"),
    url(r'^greensmow/new/', views.greensmowNew,
        name="greensmow_new"),
    url(r'^greensmow/', views.greensmowIndex, name="greensmow_index"),
    
    url(r'^', views.index, name="index"),
]
