from django.contrib import admin
from .models import Emails, Contacts, Message

# Register your models here.
admin.site.register(Emails)
admin.site.register(Contacts)
admin.site.register(Message)

