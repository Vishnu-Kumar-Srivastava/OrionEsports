from django.shortcuts import render
from .models import Team, Participant

# Create your views here.
# def index(request):
#     if (request.method=='POST'):
#         ch=request.POST.get('fav_language')
#         print(ch)
#     return render(request,'1.html')

def register(request):
    if (request.method=='POST'):
        team_name=request.POST.get('team_name')
        game=request.POST.get('GAME')
        tl_email=request.POST.get('Email')
        phone = request.POST.get('Phno')
        if (Team.objects.filter(team_name=team_name).exists()):
            return render(request,'message.html',{'message':'Team Name already exists'})
        if (Team.objects.filter(email=tl_email).exists()):
            return render(request,'message.html',{'message':'Email already exists'})
        
        tl_name=request.POST.get('name')
        tl_rollno=request.POST.get('rollno')
        tl_branch=request.POST.get('Branch')
        tl_year=request.POST.get('YEAR')
        tl_id=request.POST.get('ID')
        if (Participant.objects.filter(roll=tl_rollno).exists()):
            return render(request,'message.html',{'message':'Team Leader Roll number already exists'})
        
        p1_name=request.POST.get('NAME1')
        p1_rollno=request.POST.get('ROLLNO1')
        p1_branch=request.POST.get('Branch1')
        p1_year=request.POST.get('YEAR1')
        p1_id=request.POST.get('ID1')
        if (Participant.objects.filter(roll=p1_rollno).exists()):
            return render(request,'message.html',{'message':'Player 1 Roll number already exists'})
            
        p2_name=request.POST.get('NAME2')
        p2_rollno=request.POST.get('ROLLNO2')
        p2_branch=request.POST.get('Branch2')
        p2_year=request.POST.get('YEAR2')
        p2_id=request.POST.get('ID2')
        if (Participant.objects.filter(roll=p2_rollno).exists()):
            return render(request,'message.html',{'message':'Player 2 Roll number already exists'})
        
        p3_name=request.POST.get('NAME3')
        p3_rollno=request.POST.get('ROLLNO3')
        p3_branch=request.POST.get('Branch3')
        p3_year=request.POST.get('YEAR3')
        p3_id=request.POST.get('ID3')
        if (Participant.objects.filter(roll=p3_rollno).exists()):
            return render(request,'message.html',{'message':'Player 3 Roll number already exists'})
        
        p4_name=request.POST.get('NAME4')
        p4_rollno=request.POST.get('ROLLNO4')
        p4_branch=request.POST.get('Branch4')
        p4_year=request.POST.get('YEAR4')
        p4_id=request.POST.get('ID4')
        if (Participant.objects.filter(roll=p4_rollno).exists()):
            return render(request,'message.html',{'message':'Player 4 Roll number already exists'})
        
        team = Team(team_name=team_name,game=game,email=tl_email, phone=phone)
        team.save()
        tl = Participant.objects.create(name=tl_name,roll=tl_rollno,branch=tl_branch,year=tl_year,game_id=tl_id,team=Team.objects.get(team_name=team_name))
        tl.save()
        p1 = Participant.objects.create(name=p1_name,roll=p1_rollno,branch=p1_branch,year=p1_year,game_id=p1_id,team=Team.objects.get(team_name=team_name))
        p1.save()
        p2 = Participant.objects.create(name=p2_name,roll=p2_rollno,branch=p2_branch,year=p2_year,game_id=p2_id,team=Team.objects.get(team_name=team_name))
        p2.save()
        p3 = Participant.objects.create(name=p3_name,roll=p3_rollno,branch=p3_branch,year=p3_year,game_id=p3_id,team=Team.objects.get(team_name=team_name))
        p3.save()
        p4 = Participant.objects.create(name=p4_name,roll=p4_rollno,branch=p4_branch,year=p4_year,game_id=p4_id,team=Team.objects.get(team_name=team_name))
        p4.save()
        return render(request,'message.html',{'message':'Registration Successful'})
    
    return render(request,'esports.html')

def FIFA(request):
    if (request.method=='POST'):
        email = request.POST.get('email')
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        branch = request.POST.get('Branch')
        year = request.POST.get('YEAR')
        game_id = request.POST.get('ID1')
        phone = request.POST.get('Phno')
        
        if (Participant.objects.filter(roll=rollno).exists()):
            player = Participant.objects.get(roll=rollno)
            player.FIFA = True
            player.save()
        else:
            player = Participant.objects.create(name=name,roll=rollno,branch=branch,year=year,FIFA=True,game_id=game_id)
            player.save()
        Team.objects.create(team_name=name+"_"+rollno,game='FIFA',email=email, phone=phone)
        return render(request,'message.html',{'message':'Registration Successful'})
    return render(request,'fifa.html')

def message(request,mess):
    return render(request,'message.html',{'message':mess})

