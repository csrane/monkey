#blog/models.py
import re
from django.forms import ValidationError
from django.db import models


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    author = models.CharField(max_length=20, verbose_name = '작성자') 
    title = models.CharField(max_length=100, verbose_name = '제목', help_text = "제목을 입력하시오. 최대 100자 내외")
    content = models.TextField(verbose_name = '내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, 
        validators = [lnglat_validator],
        help_text='경도/위도 포멧으로 입력하시오')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title