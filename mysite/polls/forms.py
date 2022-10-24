from django import forms
from .models import Post

class SelectQueryForm(forms.Form):
    QUERY_1 = 'query_1'
    QUERY_2 = 'query_2'
    QUERY_3 = 'query_3'
    QUERY_4 = 'query_4'
    QUERY_5 = 'query_5'
    QUERY_6 = 'query_6'
    QUERY_7 = 'query_7'
    QUERY_8 = 'query_8'
    QUERY_9 = 'query_9'
    QUERY_10 = 'query_10'
    QUERY_11 = 'query_11'
    QUERY_12 = 'query_12'
    QUERY_13 = 'query_13'
    QUERY_14 = 'query_14'
    QUERY_15 = 'query_15'
    QUERY_16 = 'query_16'
    QUERY_17 = 'query_17'
    QUERY_18 = 'query_18'
    QUERY_19 = 'query_19'
    QUERY_20 = 'query_20'
    QUERY_21 = 'query_21'
    QUERY_22 = 'query_22'

    QUERY_CHOICES = (
        (QUERY_1, u"Query 1"),
        (QUERY_2, u"Query 2"),
        (QUERY_3, u"Query 3"),
        (QUERY_4, u"Query 4"),
        (QUERY_5, u"Query 5"),
        (QUERY_6, u"Query 6"),
        (QUERY_7, u"Query 7"),
        (QUERY_8, u"Query 8"),
        (QUERY_9, u"Query 9"),
        (QUERY_10, u"Query 10"),
        (QUERY_11, u"Query 11"),
        (QUERY_12, u"Query 12"),
        (QUERY_13, u"Query 13"),
        (QUERY_14, u"Query 14"),
        (QUERY_15, u"Query 15"),
        (QUERY_16, u"Query 16"),
        (QUERY_17, u"Query 17"),
        (QUERY_18, u"Query 18"),
        (QUERY_19, u"Query 19"),
        (QUERY_20, u"Query 20"),
        (QUERY_21, u"Query 21"),
        (QUERY_22, u"Query 22"),
    )
    querys = forms.ChoiceField(choices=QUERY_CHOICES)

    # def select_query(self,form):



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)