from django.urls import path
from . import views
urlpatterns=[
path('about',views.about,name="about"),
path('home',views.home,name="home"),
path('officelist',views.officelist,name="officelist"),
path('snaps',views.snaps,name="snaps"),
path('past',views.past,name="past"),
path('individualeventspics',views.individualeventspics,name="individualeventspics"),
path('academic20_21',views.academic20_21,name="academic20_21"),
path('winners/<int:id>',views.win,name="winners"),
path('upcoming',views.upcoming,name="upcoming"),
path('contact',views.contact,name="contact"),
path('contactpage',views.contactsendmail,name="contactpage"),
path('registrations',views.registrations,name="registrations"),
path('eventregistration',views.eventregistration,name="eventregistration")
]
