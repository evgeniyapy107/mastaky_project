from django.contrib import admin
from . import models


admin.site.register(models.Education)
admin.site.register(models.EducationDetail)
admin.site.register(models.MK)
admin.site.register(models.MkDetail)
admin.site.register(models.StudentWork)
admin.site.register(models.Feedback)

# Register your models here.
