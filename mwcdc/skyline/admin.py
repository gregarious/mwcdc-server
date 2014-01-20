from skyline.models import InterestPoint, Viewpoint, InterestPointMapping
from django.contrib import admin

class InterestPointAdmin(admin.ModelAdmin):
	exclude = ('address',)		# no real need for this data
	ordering = ('name',)

admin.site.register(InterestPoint, InterestPointAdmin)
admin.site.register(InterestPointMapping)

# we're hardcoding this data on the app itself
# admin.site.register(Viewpoint)
