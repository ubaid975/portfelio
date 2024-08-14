from django.contrib import admin
from portfelio.models import contact


# Register your models here.
@admin.register(contact)
class contactus(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','email','message']

