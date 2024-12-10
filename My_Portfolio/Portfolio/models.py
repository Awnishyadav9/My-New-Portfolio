from django.db import models
# user- Awnishyadav
#pass - Yadav@4455

class QueryData(models.Model):
    name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_query = models.TextField()
    

    def __str__(self):
        return self.name 

