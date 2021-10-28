from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from PIL import Image
from io import BytesIO
from django.core.files import File


# County model


class County(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.pk}-{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/{self.pk}/"


# SubCounty model
class Subcounty(models.Model):
    name = models.CharField(max_length=30)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='subcounties')
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.id}-{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def get_county(self):
        if self.county:
            return f"{self.county.name}"
        return ""

# Category model


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.id}-{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

# Poultry


class Poultry(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sells', null=True)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='poultries')
    image = models.ImageField(upload_to='poultry_images/')
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='poultries')
    subcounty = models.ForeignKey(
        Subcounty, on_delete=models.CASCADE, related_name='poultries')
    location = models.CharField(max_length=100)
    business_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    price = models.CharField(max_length=50, default="Negotiable")
    date_posted = models.DateField(auto_now=True)
    approved = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    views = models.IntegerField(default=1)

    class Meta:
        ordering = ('-date_posted', '-id')

    def __str__(self):
        return f"{self.pk},{self.title},{self.date_posted},{self.price},{self.views}"

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}"

    def get_image(self):
        if self.image:
            return self.image.url
        return ""

    def get_county(self):
        if self.county:
            return f"{self.county.name}"
        return ""

    def get_subcounty(self):
        if self.subcounty:
            return f"{self.subcounty.name}"
        return ""
