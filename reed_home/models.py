from django.db import models

class Job(models.Model):
    company_name = models.CharField(max_length=50, blank = True, null = True)
    job_title = models.CharField(max_length=50, blank = True, null = True)
    location = models.CharField(max_length=20, blank = True, null = True)
    description = models.CharField(max_length=4000, blank = True, null = True)

    def __str__(self):
        return self.name


