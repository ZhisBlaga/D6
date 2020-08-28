from django.db import models

# Create your models here.

class Friend(models.Model):
    friend_name = models.TextField()

    def __str__(self):
        return self.friend_name

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class PublishingHouse(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        Friend, blank=True, 
    )

    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    publisher = models.ForeignKey(PublishingHouse, on_delete=models.DO_NOTHING, null=True, blank=True)
    img = models.ImageField(upload_to='book_img/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url


