from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    performer = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=500)
    embed_url = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="Images/videos/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.CharField(max_length=1000, blank=True)
    article_img = models.ImageField(upload_to="Images/articles/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    place = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="Images/activities/", default="Image/None/Noimg.jpg")
    description = models.CharField(max_length=3000)
    program = models.JSONField(default=list)
    ticket = models.JSONField(default=list)

    def __str__(self):
        return self.title


class IndexStory(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    place = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="Images/index_stories/", default="Image/None/Noimg.jpg")
    url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    date = models.DateField()
    experience = models.CharField(max_length=3000)

    def __str__(self):
        return self.experience

#  TODO自定義將description變多行
class Teacher(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="Images/teachers/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title


class Albums(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateField()
    indexImage = models.ImageField(upload_to="Images/albums/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title
