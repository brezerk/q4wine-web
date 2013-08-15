from django.db import models

class News(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length = 128)
    content = models.TextField()

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name_plural = 'News'
