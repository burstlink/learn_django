from django.db import models

# 定义模型 - 也就是数据库结构设计和附加的其它元数据
# 每个模型都是models.Model的子类，每个model类的变量表示数据库里的一个字段
# 根据model的代码 django可以生产创建数据库的schema语句，创建和类对象数据交互的数据库api(对象关系映射)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
