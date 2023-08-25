from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    signin_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff_images/')
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

class VisitorDetails(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    reason = models.TextField()
    state = models.CharField(max_length=20)  # For example: "Confirmed" or "Pending"
    visiting_datetime = models.DateTimeField(auto_now_add=True)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='drink_images/')
    serve_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)

class VisitorDrink(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    state = models.CharField(max_length=20)  # For example: "Pending" or "Served"
    serve_datetime = models.DateTimeField(auto_now_add=True)
