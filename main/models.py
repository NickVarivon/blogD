from django.db import models



class Blogs(models.Model):
    title = models.CharField(max_length=500)
    short_text = models.CharField(max_length=1000)
    text = models.CharField(max_length=50000)
    image = models.ImageField(upload_to="images/")
    time_create = models.TimeField(auto_now_add=True)
    data_create = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    comment = models.ForeignKey('Commentaries', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Commentaries(models.Model):
    text_comment = models.CharField(max_length=500)
    count = models.IntegerField(default=0)


class CountView(models.Model):
    count = models.IntegerField(default=0)