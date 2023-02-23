from django.db import models
from app.models.universities import Universities
from app.models.department import Department

class DepartmentMiddle(models.Model):
    university_id = models.ForeignKey(Universities, on_delete=models.DO_NOTHING)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'department_middle'