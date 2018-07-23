from django.db import models


# Create your models here.
class Test(models.Model):
    tid = models.AutoField('ID', primary_key=True)
    name = models.CharField('姓名', max_length=64, unique=True)

    class Meta:
        verbose_name = '测试'
        verbose_name_plural = verbose_name
        db_table = 'tb_test'
