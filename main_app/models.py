from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# County model


class County(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.id}-{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/{self.id}/"


# SubCounty model
class Subcounty(models.Model):
    name = models.CharField(max_length=15)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='subcounties')
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ('name',)

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
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=20)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.id}-{self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

# Poultry


class Poultry(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=20)
    description = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='poultries')
    image = models.ImageField(upload_to='poultry_images/')
    thumbnail = models.ImageField(
        upload_to='poultry_images/', blank=True, null=True)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='poultries')
    subcounty = models.ForeignKey(
        Subcounty, on_delete=models.CASCADE, related_name='poultries')
    price = models.CharField(max_length=25, default="Negotiable")
    date_posted = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f"{self.id}-{self.title}, {self.date_posted}, {self.price}"

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 148)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, image.name)

        return thumbnail

    def get_county(self):
        if self.county:
            return f"{self.county.name}"
        return ""

    def get_subcounty(self):
        if self.subcounty:
            return f"{self.subcounty.name}"
        return ""
