from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

class Category(models.Model):
    category = models.CharField(max_length= 30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()
    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    def delete_category(self):
        self.delete()  
    
    

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', null=True,blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,category):
        category = cls.objects.filter(category__category__icontains = category)
        return category

    @classmethod
    def filter_by_location(cls,location):
        # location = Location.objects.get(name = search_term)
        location = cls.objects.filter(location__location= location).all()
        return location
    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value)
        
    class Meta:
        ordering = ['name']

