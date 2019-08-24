from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

    def ___str___(self):
        return str(self.pk)+''+self.name


class Publications(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Books(model.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=10)
    authors = models.ManyToManyField('Authors', related_name='books')
    publication = models.ForeignKey('Publications', related_name='books')
    pages = models.IntegerField()
    price = models.DecimalField(max_length=10, decimal_places=2)

    def __str__(self):
        return self.name
