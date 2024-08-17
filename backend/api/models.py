from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    performer = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=500)
    embed_url = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="Images/videos/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "影片"  # 自定義單數形式的名稱
        verbose_name_plural = "影片列表"  # 自定義複數形式的名稱


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField(blank=True)
    tag = models.JSONField()
    article_img = models.ImageField(upload_to="Images/articles/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"  # 自定義單數形式的名稱
        verbose_name_plural = "文章列表"  # 自定義複數形式的名稱


class Activity(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    place = models.CharField(max_length=100)
    price_type = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="Images/activities/", default="Image/None/Noimg.jpg")
    description = models.TextField()
    program = models.JSONField(default=list)
    ticket = models.JSONField(default=list)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "活動"  # 自定義單數形式的名稱
        verbose_name_plural = "活動列表"  # 自定義複數形式的名稱


class IndexStory(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    place = models.CharField(max_length=100, blank=True)
    btn_text = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="Images/index_stories/", default="Image/None/Noimg.jpg")
    url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "封面故事"  # 自定義單數形式的名稱
        verbose_name_plural = "封面故事列表"  # 自定義複數形式的名稱


class Experience(models.Model):
    date = models.DateField()
    experience = models.TextField()

    def __str__(self):
        return self.experience

    class Meta:
        verbose_name = "經歷"  # 自定義單數形式的名稱
        verbose_name_plural = "經歷列表"  # 自定義複數形式的名稱


class Teacher(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="Images/teachers/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "老師"  # 自定義單數形式的名稱
        verbose_name_plural = "老師列表"  # 自定義複數形式的名稱


class Album(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateField()
    description = models.TextField(blank=True)
    tag = models.JSONField()
    indexImage = models.ImageField(upload_to="Images/albums/", default="Image/None/Noimg.jpg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "相簿"  # 自定義單數形式的名稱
        verbose_name_plural = "相簿列表"  # 自定義複數形式的名稱
