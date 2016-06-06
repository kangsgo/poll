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



admin.site.register(Question,QuestionAdmin)