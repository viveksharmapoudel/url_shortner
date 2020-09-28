from django.db import models

# Create your models here.


class ShortURL(models.Model):
    """
    Description: Model Description
    """
    url= models.URLField(max_length=500)
    unique_id= models.SlugField(max_length=7, primary_key=True)
    count=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,auto_now=False)
    deleted_at=models.DateTimeField(null=True,blank=True)
    
    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
    	return str(self.url)
    
    def __unicode__(self):
    	return str(self.url)
    	

