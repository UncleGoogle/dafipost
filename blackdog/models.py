from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Bark(models.Model):
    pub_date = models.DateField()
    content = models.CharField(max_length=160)
    reporter = models.ForeignKey(Dog, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.content
