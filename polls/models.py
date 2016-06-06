#coding=utf-8
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


#add Question data
class Question(models.Model):
	"""question_text:Text
	pub_date:Date"""
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def  __unicode__(self):
		return self.question_text
	def was_published_recently(self):
		return	self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	#list 
 	was_published_recently.admin_order_field = 'pub_date'
 	#picture : True
	was_published_recently.boolean = True
	#标题
	was_published_recently.short_description = 'Published recently?'


#add Choice date
class Choice(models.Model):
	"""Question relate question"""
	question=models.ForeignKey(Question)
	Choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __unicode__(self):
		return self.Choice_text
