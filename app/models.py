from django.db import models
from django.conf.urls.static import static
from django.urls import reverse
# Create your models here.


class ProfileData(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    bio = models.TextField()

    def __str__(self):
        return self.full_name
    
class SocialLink(models.Model):
    url = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    order = models.IntegerField(default=1)


    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name
    

class About(models.Model):
    bio = models.TextField()
    projects = models.IntegerField(default=1)
    money = models.IntegerField(default=1)
    valunteers = models.IntegerField(default=1)



    

class Tools(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField(default=1)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ('order',)


    def __str__(self):
        return self.title
# clients
class Service(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # CASCADE - 


class PostCategorys(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50)        


class Post(models.Model):
    image = models.ImageField(upload_to="posts/")
    name = models.CharField(max_length=50)
    category = models.ForeignKey(PostCategorys, on_delete=models.PROTECT) # PROTECT - saqlash
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    short_decription = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.id})
    
    
    def __str__(self):
        return self.name