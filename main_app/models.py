from django.db import models

# Create your models here.

# County model
class County(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"
    
# SubCounty model
class Subcounty(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"

# Category model
class Category(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"

# Poultry 
class Poultry(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='poultry_images/')
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='counties')
    subcounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE, related_name='subcounties')
    price = models.CharField(max_length=25, default="Negotiable")
    date_posted = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['date_posted']
    
    
    def __str__(self):
        return f"{self.name}, {self.date_posted}, {price}"
