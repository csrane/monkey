#blog/models.py
import re

from django.core.urlresolvers import reverse
from django.conf import settings
from django.forms import ValidationError
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_post_set')
    title = models.CharField(max_length=100, verbose_name = '제목', help_text = "제목을 입력하시오. 최대 100자 내외")
    content = models.TextField(verbose_name = '내용')
    photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d' )
    photo_thumbnail = ImageSpecField(source='photo',
                                    processors=[Thumbnail(300,300)],
                                    format='JPEG',
                                    options={'qualit':60})

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, 
        validators = [lnglat_validator],
        help_text='경도/위도 포멧으로 입력하시오')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id'] #기본정렬 순서 지정 


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name 