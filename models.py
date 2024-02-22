from django.db import models

class Topic(models.Model):
	""" 用户学习的主题"""
	# 创建一个字符组成的数据，并且设置了存储字符上限 200
	text = models.CharField(max_length=200)
	# 创建一个记录日期和时间的数据时间戳，auto_now_add=True 自动用当前时间。
	date_added = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
	""" 日志文档类"""
	# 关联主题外键,on_delete=models.CASCADE 当关联的Topic对象被删除时，所有的Entry对象也会被删除。
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	# 创建一个文本文件实例
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		""" 返回模型的字符串表示"""
		if len(self.text) > 50:
			return self.text[:50] + "..."
		else:
			return self.text[:50]
















