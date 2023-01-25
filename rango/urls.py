# importing url mapping machinery
from django.urls import path
# importing views module from rango app
from rango import views

app_name = 'rango'
# python list[]
urlpatterns = [
    # path function - first parameter is string of URL, second is the view that will be called if a match is found, third is name
    path('',views.index, name= 'index'),
    # remember to include final / 
    path('about/',views.about, name= 'about')
]