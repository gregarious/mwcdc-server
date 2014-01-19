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

	interest_points = models.ManyToManyField(InterestPoint, through='InterestPointMapping')

	def __unicode__(self):
		return self.name


class InterestPointMapping(models.Model):
	viewpoint = models.ForeignKey(Viewpoint)
	interest_point = models.ForeignKey(InterestPoint)

	x = models.IntegerField(help_text="x-coordinate of point on viewpoint image")
	y = models.IntegerField(help_text="y-coordinate of point on viewpoint image")

	def __unicode__(self):
		return "%s: %s" % (unicode(self.interest_point), unicode(self.viewpoint))
