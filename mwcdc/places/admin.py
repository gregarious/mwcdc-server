from places.models import Place
from django.contrib import admin

class PlaceModelAdmin(admin.ModelAdmin):
	exclude = ('category_id', 'external_image_url',)
	ordering = ('name',)

	def get_readonly_fields(self, request, obj=None):
		if not request.user.is_superuser:
			return ('name', 'street_address', 'image', 'description', 'hours',
				'fb_id', 'twitter_handle', 'zip_code', 'phone', 'contact_email',
				'website', 'category_label')
		else:
			return tuple()

admin.site.register(Place, PlaceModelAdmin)
