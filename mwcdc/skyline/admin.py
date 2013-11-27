from skyline.models import InterestPoint, Viewpoint, InterestPointMapping
from django.contrib import admin

class InterestPointAdmin(admin.ModelAdmin):
	ordering = ('name',)

admin.site.register(InterestPoint, InterestPointAdmin)
admin.site.register(Viewpoint)
admin.site.register(InterestPointMapping)
