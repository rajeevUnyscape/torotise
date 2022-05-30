from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Partner(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)
    email = models.CharField(max_length=200,null = True, blank = True)
    phone_number = models.CharField(max_length=200,null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name ="partner_creator",default="1")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="partner_updator",default="1")

    def __str__(self):
        return str(self.id)


class Plans(models.Model):
    plan_name = models.CharField(max_length=200, null = True, blank = True)
    amount_options = models.CharField(max_length=200,null = True, blank = True)
    tenure_options = models.CharField(max_length=200,null = True, blank = True)
    benefit_percentage = models.CharField(max_length=200,null = True, blank = True)
    benefit_type = models.CharField(max_length=200,null = True, blank = True)
    status = models.CharField(max_length=200,null = True, blank = True)
    description = models.CharField(max_length=200,null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(Partner, on_delete=models.CASCADE,related_name ="plan_creator",default="1")
    updated_by = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name ="plan_updator",default="1")

    def __str__(self):
        return str(self.id)


class Promotion(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE,related_name ="promotion_plan",default="1")
    no_of_user = models.CharField(max_length=200,null = True, blank = True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200,null = True, blank = True)
    benefit_percentage = models.CharField(max_length=200,null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name ="promotion_creator",default="1")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="promotion_updator",default="1")

    def __str__(self):
        return str(self.id)

class CustomerGoals(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE,related_name ="customer_plan",default="1")
    selected_amount = models.CharField(max_length=200,null = True, blank = True)
    selected_tenure = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    deposited_amount = models.CharField(max_length=200,null = True, blank = True)
    benefit_percentage = models.CharField(max_length=200,null = True, blank = True)
    benefit_type = models.CharField(max_length=200,null = True, blank = True)
    description = models.CharField(max_length=200,null = True, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name ="customer_creator",default="1")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="customer_updator",default="1")

    def __str__(self):
        return str(self.id)


