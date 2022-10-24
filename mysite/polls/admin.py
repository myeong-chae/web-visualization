from django.contrib import admin

from .models import Choice, Data, Question, Product, Post, TPC_H_QUERY, Side_Var


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Product)
admin.site.register(Data)
admin.site.register(Post)
admin.site.register(TPC_H_QUERY)
admin.site.register(Side_Var)
# Register your models here.
