from django.db import models
from django.utils import timezone
import datetime

# 定义模型 - 也就是数据库结构设计和附加的其它元数据
# 每个模型都是models.Model的子类，每个model类的变量表示数据库里的一个字段
# 根据model的代码 django可以生产创建数据库的schema语句，创建和类对象数据交互的数据库api(对象关系映射)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
