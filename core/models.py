from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation
