from django.contrib import admin
from .models import Team, Participant
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import AdminSite
from import_export.admin import ExportMixin



class TeamResource(resources.ModelResource):
    class Meta:
        model = Team
        
class TeamAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TeamResource
    list_display = ['team_name','game','email']
    list_filter = ['game']
    search_fields = ['team_name','game','email']
    
admin.site.register(Team, TeamAdmin)
class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant
        fields = ('name','roll','branch','year','game_id','team__team_name','team__game','FIFA','VALO','CODM')
class ParticipantAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ParticipantResource
    list_display = ['name','roll','team','branch','year','game_id','FIFA','VALO','CODM']
    list_filter = ['FIFA','VALO','CODM','team__game']
    search_fields = ['name','roll','branch','year','game_id']



admin.site.register(Participant, ParticipantAdmin)

# admin.site.register(Team)
# admin.site.register(Participant)
