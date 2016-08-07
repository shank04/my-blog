from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now,
             null=True )
    is_liked=models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
     	return reverse('post_list')

    def __str__(self):
        return self.text