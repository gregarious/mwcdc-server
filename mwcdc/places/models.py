from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Place(models.Model):
	name = models.CharField(max_length=50)
	street_address = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
	image = ThumbnailerImageField(blank=True, upload_to='images')

	description = models.TextField(blank=True)
	hours = models.TextField(blank=True)
	fb_id = models.CharField(max_length=200, blank=True)
	twitter_handle = models.CharField(max_length=32, blank=True)
	zip_code = models.CharField(max_length=10, default='15211', blank=True)
	phone = models.CharField(max_length=20, blank=True)
	contact_email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	
	category_id = models.IntegerField()
	category_label = models.CharField(max_length=20)

	# temporary field in place of `image` until image importing is in place
	external_image_url = models.URLField(blank=True)

	def __unicode__(self):
		return self.name
