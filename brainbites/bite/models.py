from django.db import models


#Tag object
class Tag(models.Model):
	"""class to handle tags"""
	tagName = models.CharField(max_length=128)

#Author object
class Author(models.Model):
	"""class to handle authors"""
	authorName = models.CharField(max_length=128)


# Bite object
class Bite(models.Model):
    """The primary class for bite data"""
    title = models.TextField()    
    explination = models.TextField()
    link = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    #picture = models.FileField()




