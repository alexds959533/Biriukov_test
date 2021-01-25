from django.db import models


class City(models.Model):
    """Города"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Street(models.Model):
    """Улицы"""

    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    """Магазины"""

    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    building = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


