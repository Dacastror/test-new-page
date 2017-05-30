from django.db import models
from django.utils import timezone
from mezzanine.pages.models import Page, PageMoveException

class Topico(Page):

    def can_delete(self, request):
        return request.user.is_superuser or self.parent is not None

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
