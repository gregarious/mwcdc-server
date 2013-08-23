from places.models import Place
from django.contrib import admin
from django import forms
from django.contrib import messages

class PlaceModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('name', 'address', 'image', 'description', 'hours',
                'fb_id', 'twitter_id', 'zip_code', 'phone', 'contact_email',
                'website', 'category')
        else:
            return tuple()

admin.site.register(Place, PlaceModelAdmin)
