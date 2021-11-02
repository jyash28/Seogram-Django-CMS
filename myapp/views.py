from myapp.forms import DataForm
# from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

# Create your views here.


class DataView(generic.CreateView):
    form_class = DataForm
    template_name = 'contact.html'

    def form_valid(self, form):
        self.object = form.save()
        # return redirect(reverse('myapp:data'))
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

#
# class ServicesView(TemplateView):
#     template_name = 'service.html'



