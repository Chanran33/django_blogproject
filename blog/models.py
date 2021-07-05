from django.db import models

# Create your models here.
class Blog(models.Model):
    objects = models.Manager() #class has no objects member에러가 난다면 django 기본 모델 매니저를 추가해준다.
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank = True, null = True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]