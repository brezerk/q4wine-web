from django.db import models

class Doc(models.Model):
    title = models.CharField(max_length = 128)
    slug = models.SlugField(max_length = 128)
    language = models.CharField(max_length = 32)
    text = models.TextField()

    class Meta:
        unique_together = ('slug', 'language')

    def get_absolute_url(self):
        return "/documentation/" + self.language + "/" + self.slug + ".html"
