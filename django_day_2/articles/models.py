from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f"{self.created_at.month}/{self.created_at.day}일에 생성된 {self.id}번글 - {self.title} : {self.content}"


# 월/일에 생성된 id번글 - title : content 형식 (created_at.month, created_at.day로 월/일 호출)