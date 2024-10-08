# Generated by Django 5.1 on 2024-08-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('poster', models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/activities/')),
                ('description', models.CharField(max_length=3000)),
                ('program', models.JSONField(default=list)),
                ('ticket', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('indexImage', models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/albums/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('article_img', models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/articles/')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('experience', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='IndexStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('place', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/index_stories/')),
                ('url', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
