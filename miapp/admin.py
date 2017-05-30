from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Topico

admin.site.register(Topico, PageAdmin)
