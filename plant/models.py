from django.db import models

class Plant(models.Model):
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.scientific_name

class LocalPlant(models.Model):
    plant = models.ForeignKey(Plant)
    common_name = models.CharField(max_length=100, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        if self.common_name:
            return self.common_name
        else:
            return "blank"

class Tag(models.Model):
    plants = models.ManyToManyField(LocalPlant)
    name = models.CharField(max_length=30)
    color = models.IntegerField()
    def __str__(self):
        return self.name

class Zone(models.Model):
    plants = models.ManyToManyField(LocalPlant)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Cultivar(models.Model):
    name = models.CharField(max_length=30)
    notes = models.TextField(null=True, blank=True)
    local_plant = models.ForeignKey(LocalPlant)
    def __str__(self):
        return self.name
