from django.db import models

STATUS = [("PROGRESS","PROGRESS"), ("COMPLETED","COMPLETED")]

BILLABLE_TO = [("test1","test1"), ("test2","test2")]

USERS_TEMP_DEV = [("USER1","USER1"),("USER2","USER2")]

class Activities(models.Model):
    description = models.CharField(max_length=200)
    client_code = models.CharField(max_length=10, blank="true")
    due_date = models.DateField()
    assignment = models.CharField(max_length=10,  choices=USERS_TEMP_DEV)
    status = models.CharField(max_length=10, choices=STATUS)
    effort = models.IntegerField()
    billable_to = models.CharField(max_length=10,choices=BILLABLE_TO)
    invoiced = models.BooleanField()

    class Meta:
        unique_together = ('description', 'client_code')

