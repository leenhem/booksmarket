from django.db import models

# Create your models here.

# class Article(models.Model):
#     title = models.CharField(u'标题',max_length=256)
#     content = models.TextField(u'内容')
#     pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
#     update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
sex_choices=(
    ('f','famale'),
    ('m','male'),
)
class Employee(models.Model):   #类名就是表名，表名为小写
    name = models.CharField(max_length=20)  #字段名
    def __str__(self):
        return self.name
class Blog(models.Model):
    name=models.CharField(max_length=30)
    employee=models.ForeignKey(Employee)#employee对象中封装id name
    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=1,choices=sex_choices)

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Book(models.Model):
    name=models.CharField(max_length=30)
    authors=models.ManyToManyField(Author)

    def __str__(self):
        return self.name