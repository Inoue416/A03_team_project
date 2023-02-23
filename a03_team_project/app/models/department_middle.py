from django.db import models
from app.models.universities import Universities
from app.models.department import Department

class DepartmentMiddle(models.Model):
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'department_middle'