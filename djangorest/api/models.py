from django.db import models

class Bucketlist(models.Model):
    """ This class represents the bucketlist model. """
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    	""" Return a human redable representation of the object instance."""
    	return "{}".format(self.name)