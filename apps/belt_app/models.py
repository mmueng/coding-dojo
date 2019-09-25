from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from datetime import datetime
import datetime
from datetime import date
from apps.login_app.models import User


class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if(postData['title'] is None or postData['title'] is ''):
            errors["title"] = "Title field is Required."
        elif len(postData['title']) < 3:
            errors["title"] = "Title should be at least 2 characters"

        if(postData['desc'] is None or postData['desc'] is ''):
            errors["desc"] = "Description field is Required."
        elif len(postData['desc']) < 3:
            errors["desc"] = "Description should be at least 2 characters"

        if(postData['location'] is None or postData['location'] is ''):
            errors["location"] = "location field is Required."
        elif len(postData['location']) < 3:
            errors["location"] = "location should be at least 2 characters"

        # if(postData['category'] is None or postData['category'] is ''):
        #     errors["category"] = "category field is Required."
        # elif len(postData['category']) < 3:
        #     errors["category"] = "category should be at least 2 characters"
        return errors

    def job_validatoradd(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if(postData['title'] is None or postData['title'] is ''):
            errors["title"] = "Title field is Required."
        elif len(postData['title']) < 3:
            errors["title"] = "Title should be at least 2 characters"

        if(postData['desc'] is None or postData['desc'] is ''):
            errors["desc"] = "Description field is Required."
        elif len(postData['desc']) < 3:
            errors["desc"] = "Description should be at least 2 characters"

        if(postData['location'] is None or postData['location'] is ''):
            errors["location"] = "location field is Required."
        elif len(postData['location']) < 3:
            errors["location"] = "location should be at least 2 characters"

        # if(postData['category'] is None):
        #     errors["category"] = "category field is Required."

        return errors


class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    category2 = models.CharField(max_length=255)
    category3 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='created_job')
    job_user = models.ManyToManyField(User, related_name='job_joined')
    objects = JobManager()
