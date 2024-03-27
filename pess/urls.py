from pess import views as pass_views
from django.urls import path
app_name = 'pess'

urlpatterns = [
    path('',pass_views.pess,name="pess"),
]