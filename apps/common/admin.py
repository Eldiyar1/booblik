from django_summernote.models import Attachment
from django.contrib import admin

if admin.site.is_registered(Attachment):
    admin.site.unregister(Attachment)
