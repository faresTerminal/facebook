from django.shortcuts import reverse, Http404
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField
import hashlib

from django.utils import timezone 
from django.template.defaultfilters import slugify


from django.conf import settings





def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(" ' ", "-")
    str = str.replace('"', '-')
    str = str.replace(" ّ ", "-")
    str = str.replace(".", "")
    str = str.replace("،", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str




# Create your models here.

class articles(models.Model):
   
    title = models.CharField('العنوان', max_length=9500, null=True, blank = True)
    slug = models.SlugField(max_length=9500, unique_for_date='publish', allow_unicode=True)
    image = models.ImageField('صورة مناسبة', upload_to = 'Images', null=True, blank = True)
   

    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
  
    publish = models.DateTimeField(default=timezone.now) 


   
    
    
    
    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
    
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)

        super(articles, self).save(*args, **kwargs)

   

    

    


    def get_absolute_url(self):
        return reverse('fishing:show_article', kwargs={'id':self.id, 'slug': self.slug})
    

   
