from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ArticleAdmin(SummernoteModelAdmin):
    model = Article

class NewsAdmin(SummernoteModelAdmin):
    model = News

class InlineSpecialization(admin.StackedInline):
    model = Specialization
    extra = 1

class InlineYear(admin.StackedInline):
    model = Year
    extra = 1

class InlineStatistic(admin.StackedInline):
    model = Statistic
    extra = 1

class OKRAdmin(SummernoteModelAdmin):
    model = OKR
    inlines = [InlineSpecialization, InlineStatistic, InlineYear]

class InlinePare(admin.StackedInline):
    model = Pare
    extra = 1

class Schedule_blockAdmin(SummernoteModelAdmin):
    model = Schedule_block
    inlines = [InlinePare]

class InlinePublication(admin.StackedInline):
    model = Publication
    extra = 1

class LiberyAdmin(SummernoteModelAdmin):
    model = Libery
    inlines = [InlinePublication]

class InlineOlimp_result(admin.StackedInline):
    model = Olimp_result
    extra = 1

class OlimpAdmin(SummernoteModelAdmin):
    model = Olimp
    inlines = [InlineOlimp_result]


admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Specialization)
admin.site.register(Administration)
admin.site.register(News, NewsAdmin)
admin.site.register(CustomUser)
admin.site.register(Photo)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Person)
admin.site.register(Grup)
admin.site.register(OKR, OKRAdmin)
admin.site.register(Schedule_block, Schedule_blockAdmin)
admin.site.register(Contacts)
admin.site.register(Student_action)
admin.site.register(Study_info)
admin.site.register(Libery, LiberyAdmin)
admin.site.register(Olimp, OlimpAdmin)
