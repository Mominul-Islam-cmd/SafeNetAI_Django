from django.db import models

# Create your models here.


class researcher_form(models.Model):
    id=models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    current_project = models.CharField(max_length=100)
    uv_name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=100)
    session=models.CharField(max_length=100)
    interested_domain=models.CharField(max_length=200)
    experiences=models.CharField(max_length=200)
    # join_date = models.DateField(default=datetime.date.today)
    ratings=(
    (1,"Active"),
    (2,"Very Active"),
    (3,"Hardworking"),
    (4,"Excellent Hardworking"),
    (5,"Extraordinary"),
    )
    
    Ranking=models.IntegerField(choices=ratings)

    def __str__(self):
        return f"{self.first_Name} {self.last_Name}"

class researcher_recommend(models.Model):
    researcher_id=models.ForeignKey(researcher_form,on_delete=models.CASCADE)
    Details=models.CharField(max_length=300)

    def __str__(self):
     return f"{self.researcher_id} - {str(self.Details)}"

