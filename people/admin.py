from django.contrib import admin
from .models import Role, Skill, Event, Person, PersonRole, PersonSkill, PersonEvent


class PersonRoleInline(admin.TabularInline):
    model = PersonRole
    extra = 1


class PersonSkillInline(admin.TabularInline):
    model = PersonSkill
    extra = 1


class PersonEventInline(admin.TabularInline):
    model = PersonEvent
    extra = 1


class PersonAdmin(admin.ModelAdmin):
   inlines = [PersonRoleInline, PersonSkillInline,
              PersonEventInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(Event)
admin.site.register(Skill)
admin.site.register(Role)