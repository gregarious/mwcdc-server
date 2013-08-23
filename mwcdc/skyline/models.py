from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class InterestPoint(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, blank=True, help_text='Street address only')
	description = models.TextField(blank=True)
	image = ThumbnailerImageField(blank=True, upload_to='images')

	def __unicode__(self):
		return self.name

class Viewpoint(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100, blank=True, help_text='Street address only')
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)

	skyline_image = ThumbnailerImageField(blank=True, upload_to='images')
	interest_points = models.ManyToManyField(InterestPoint, through='InterestPointMapping')

	def __unicode__(self):
		return self.name


class InterestPointMapping(models.Model):
	interest_point = models.ForeignKey(InterestPoint)
	viewpoint = models.ForeignKey(Viewpoint)

	label = models.CharField(max_length=20, help_text="Label used to help keep admins oriented")
	x = models.IntegerField(help_text="x-coordinate of point on viewpoint image")
	y = models.IntegerField(help_text="y-coordinate of point on viewpoint image")

	def __unicode__(self):
		return "%s/%s: %s" % (unicode(self.viewpoint), self.label,
			unicode(self.interest_point))
