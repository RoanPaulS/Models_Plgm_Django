from django.db import models
"""
1.Generally each model maps to a single database table.
2.Each class or model we create is a python class which is a subclass of django.db.models.Model
3.Each attribute of the model represents database field

"""

class Employee(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length = 20)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length = 100)



""" 
MIGRATION COMMANDS : 

    First we have to make the migrations i.e, we have to create the table in database , so the command is

        python manage.py makemigrations

    Second we have to migrate the data into the table that is created in database , so the command is 

        python manage.py migrate

"""


# python manage.py sqlmigrate dbApp 0001

"""
Here dbApp is the name of your App of your project

0001 is genertated automatically by django at the time of migration

"""
