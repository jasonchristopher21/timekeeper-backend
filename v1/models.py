from django.db import models
from django.utils.timezone import now

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    date = models.DateTimeField('presentation date', default=now)
    last_modified = models.DateTimeField('last modified', default=now)

    def __str__(self) -> str:
        return self.name

class Slide(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    slide_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200, default="")
    content = models.TextField()
    duration = models.DurationField()

    def __str__(self) -> str:
        return str(self.title)
