from django.contrib import admin

from agency.models import Newspaper, Redactor, Topic

admin.site.register(Newspaper)
admin.site.register(Redactor)
admin.site.register(Topic)
