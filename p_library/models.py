from django.db import models


class Author(models.Model):  
    full_name = models.CharField(max_length=255)  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publish(models.Model):
    title = models.TextField(null = True, default='')

    def __str__(self):
        return self.title


class Friend(models.Model):
    full_name = models.CharField(max_length=255, null = True, default='')

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish = models.ForeignKey(Publish, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, default='none', null=True, blank=True)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pic = models.ImageField(upload_to='books', blank=True)

    def __str__(self):
        return self.title