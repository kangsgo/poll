from django.db import models

# Create your models here.

#add Question data
class Question(models.Model):
	"""question_text:Text
	pub_date:Date"""
	question_text=models.CharField(max_length=200)
	pub_date=models.DateField('date published')
	def  __unicode__(self):
		return self.question_text


#add Choice date
class Choice(models.Model):
	"""Question relate question"""
	question=models.ForeignKey(Question)
	Choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __unicode__(self):
		return self.Choice_text
