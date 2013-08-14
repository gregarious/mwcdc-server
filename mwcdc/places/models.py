from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Place(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, help_text='Street address only')
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	image = ThumbnailerImageField(blank=True, upload_to='images')

	description = models.TextField(blank=True)
	hours = models.TextField(blank=True)
	fb_id = models.CharField(max_length=20, blank=True)
	twitter_id = models.CharField(max_length=20, blank=True)
	zip_code = models.CharField(max_length=10, default='15211')
	phone = models.CharField(max_length=20, blank=True)
	contact_email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	category = models.CharField(max_length=20, blank=True)
