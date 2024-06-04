from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = CloudinaryField('image', overwrite=True, format='jpg', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        to_assign = slugify(self.title)
        
        if App.objects.filter(slug=to_assign).exists():
            to_assign = to_assign+str(App.objects.all().count())
        
        self.slug = to_assign
        super().save(*args, **kwargs)
        


class Subscriber(models.Model):
    campaign = models.ForeignKey(App, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.email