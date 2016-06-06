#coding=utf8
from django.contrib import admin
from .models import Question,Choice

# Register your models here.
#set Choice
class ChoiceInline(admin.TabularInline):
	"""docstring for ChoiceInline"""
	model =Choice
	extra=3


#set Question
class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fieldsets=[
	     (None,                         {'fields':['question_text']}),
	     ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display=('question_text','pub_date','was_published_recently')
	#添加侧边过滤器
	list_filter = ['pub_date']
	search_fields=['question_text']




admin.site.register(Question,QuestionAdmin)