from django.db import models

# Create your models here.
class auther(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class book(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    totalpage=models.IntegerField()
    author=models.ForeignKey(auther,on_delete=models.CASCADE,related_name='author')
    def __str__(self):
        return self.title


# {
#     "phone_no":"7443564453",
#     "first_name":"Normal",
#     "last_name":"User",
#     "birthday":"2001-04-18",
#     "anniversary":"2021-03-21",
#     "tags":"Birthday",
#     "override_timezone":"IST",
#     "fields":[
#         {"custom_field_id":5,"field_data":"data"},
#         {"custom_field_id":11,"field_data":"Address"}
#         ]
# }