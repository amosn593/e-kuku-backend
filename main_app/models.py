from django.db import models
from PIL import Image
# from io import BytesIo
# from django.core.files import File

# County model


class County(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"


# SubCounty model
class Subcounty(models.Model):
    name = models.CharField(max_length=15)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='subcounties')
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

# Category model
class Category(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

# Poultry


class Poultry(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=20)
    description = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='poultries')
    image = models.ImageField(upload_to='poultry_images/')
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='poultries')
    subcounty = models.ForeignKey(
        Subcounty, on_delete=models.CASCADE, related_name='poultries')
    price = models.CharField(max_length=25, default="Negotiable")
    date_posted = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.name}, {self.date_posted}, {self.price}"

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"
