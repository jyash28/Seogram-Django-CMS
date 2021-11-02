from cms.models import CMSPlugin, Page
from filer.fields.image import FilerImageField
from django.db import models

# Create your models here.


class Card(CMSPlugin):
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, )
    title = models.CharField(max_length=255)
    description = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'CARD'
        verbose_name_plural = 'CARD'

    def __str__(self):
        return self.title


class Servicecard(CMSPlugin):
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, )
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'SERVICECARD'
        verbose_name_plural = 'SERVICECARD'

    def __str__(self):
        return self.title


class Pricecard(CMSPlugin):
    plan = models.TextField()
    price = models.FloatField()
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.plan


class Blogcard(CMSPlugin):
    blogtitle = models.TextField()
    posteddate = models.DateTimeField()
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, )

    class Meta:
        verbose_name = 'BLOGCARD'
        verbose_name_plural = 'BLOGCARD'

    def __str__(self):
        return self.blogtitle


class Contactform(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address ', max_length=255, unique=True, )
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contactform'
        verbose_name_plural = 'ContactForm'

    def __str__(self):
        return self.email






