from django.contrib.auth.models import AbstractBaseUser

from django.db import models

# from .managers import UserManager

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    game = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    # team_leader_email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    # team_leader_name = models.CharField(max_length=255, blank=False, null=False)
    # team_leader_roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    # team_leader_branch = models.CharField(max_length=100, blank=False, null=False)
    # team_leader_year = models.CharField(max_length=50, blank=False, null=False)
    # team_leader_id = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # # p1_email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    # p1_name = models.CharField(max_length=255, blank=False, null=False)
    # p1_roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    # p1_branch = models.CharField(max_length=100, blank=False, null=False)
    # p1_year = models.CharField(max_length=50, blank=False, null=False)
    # p1_id = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # # p2_email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    # p2_name = models.CharField(max_length=255, blank=False, null=False)
    # p2_roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    # p2_branch = models.CharField(max_length=100, blank=False, null=False)
    # p2_year = models.CharField(max_length=50, blank=False, null=False)
    # p2_id = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # # p3_email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    # p3_name = models.CharField(max_length=255, blank=False, null=False)
    # p3_roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    # p3_branch = models.CharField(max_length=100, blank=False, null=False)
    # p3_year = models.CharField(max_length=50, blank=False, null=False)
    # p3_id = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # # p4_email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    # p4_name = models.CharField(max_length=255, blank=False, null=False)
    # p4_roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    # p4_branch = models.CharField(max_length=100, blank=False, null=False)
    # p4_year = models.CharField(max_length=50, blank=False, null=False)
    # p4_id = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    
    
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # objects = UserManager()

    # USERNAME_FIELD = "team_name"
    # REQUIRED_FIELDS = []
    
    # def get_short_name(self):
    #     # The user is identified by their email
    #     return self.team_name
    
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    
    # def has_module_perms(self, app_label):
    #        return True
    
    def __str__(self):
        return self.team_name
    
class Participant(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default="Participant")
    roll = models.CharField(max_length=255, blank=False, null=False, unique=True)
    branch = models.CharField(max_length=100, blank=False, null=False, default=" ")
    year = models.CharField(max_length=50, blank=False, null=False, default=" 1st Year")
    # email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    game_id = models.CharField(max_length=255, blank=False, null=False, default=' ')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    VALO = models.BooleanField(default=False)
    CODM = models.BooleanField(default=False)
    FIFA = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.team:
            if self.team.game == "VALORANT":
                self.VALO = True
            elif self.team.game == "CODM":
                self.CODM = True
        super(Participant, self).save(*args, **kwargs)