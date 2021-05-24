from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import CovidCaseWebData



class CovidCaseWebDataAdmin(admin.ModelAdmin):
	ordering = ('id',)
	list_per_page = 50
	list_display =  ('country_name','total_cases','acive_cases','total_deaths', 'recovery_rate', 'pop_infected_per','created','updated')
	search_fields = ('country_name',)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(CovidCaseWebData,CovidCaseWebDataAdmin)