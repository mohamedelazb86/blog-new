from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    user=models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title=models.CharField(max_length=120,verbose_name=_('tilte'))
    content=models.TextField(_('content'),max_length=1000)
    tags = TaggableManager()
    image=models.ImageField(upload_to='photo_post')
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey('Category',related_name='post_categorry',on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)

        super(Post,self).save(*args,**kwargs)
class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user=models.CharField(max_length=120)
    post=models.ForeignKey(Post,related_name='comment_post',on_delete=models.SET_NULL,null=True,blank=True)
    content=models.TextField(max_length=300)
    publish_date=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user}----{self.post}'






