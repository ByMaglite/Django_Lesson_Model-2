from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    about_student = models.TextField(null=True, blank =True )
    image = models.ImageField(null = True, blank=True)
    
    
    def __str__(self):
        return(f"{self.number} - {self.first_name} {self.last_name}")
    
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_List"
        db_table = "Student_Table"