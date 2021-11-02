from django.urls import path
from myapp.views import DataView

app_name = 'myapp'

urlpatterns = [
    path('contact-data/', DataView.as_view(), name='data'),
    # path('new/', ServicesView.as_view(), name='new'),
]