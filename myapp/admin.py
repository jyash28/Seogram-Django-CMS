from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Card)
admin.site.register(Servicecard)
admin.site.register(Pricecard)
admin.site.register(Blogcard)


class Formadmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'subject', 'message')


admin.site.register(Contactform, Formadmin)
