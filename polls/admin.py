from django.contrib import admin

from .models import Question, Choice

admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice # 어느 모델을 가져올 것인지
    extra = 1 # 여분 작성 항목은 몇개를 기본으로 표시할 것인지


class QuestionAdmin(admin.ModelAdmin):
    # 각 필드를 구분하는 대표제목을 설정한다. (리스트 내 튜플)
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline] # 해당 클래스를 인라인으로 추가한다.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)