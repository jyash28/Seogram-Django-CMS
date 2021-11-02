from django import forms
from myapp.models import Contactform


class DataForm(forms.ModelForm):

    class Meta:
        model = Contactform
        fields = '__all__'
