from django.shortcuts import render, redirect
from django.utils import *
from .models import Goal
from datetime import datetime
import datetime


def main_login(request):
    return render(request, 'main/main_login.html')


def main_logout(request):
    return render(request, 'main/main_logout.html')


def goal_main(request):
    today = datetime.date.today()
    goals = Goal.objects.filter(deadline__gte=today)    
    return render(request, 'main/goal_main.html', {'goals':goals})


def goal_detail(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    isMember = request.user in goal.member.all()
    context = {
        'goal' : goal,
        'isMember' : isMember
    }
    return render(request, 'main/goal_detail.html', context)


def add_goal(request):
    return render(request, 'main/add_goal.html')


def create_goal(request):
    new_goal = Goal()
    new_goal.category = request.POST['category']
    new_goal.certify_method = request.POST['certify_method']
    new_goal.manager = request.user
    new_goal.name = request.POST['name']
    new_goal.description = request.POST['description']
    new_goal.created = timezone.now()
    new_goal.deadline = request.POST['deadline']
    new_goal.start_date = request.POST['start_date']
    new_goal.fee = request.POST['fee']
    new_goal.member_limit = request.POST['member_limit']
    

    request.user.profile.cash -= 500
    request.user.profile.save()
    # 인증 방식이 수치인 경우 인증 기준의 값과 단위를 db에 저장
    if request.POST['certify_method'] == 'figure':
        new_goal.criteria = request.POST['criteria']
        new_goal.value = request.POST['value']
        new_goal.unit = request.POST['unit']
    
    new_goal.save()    
    return redirect('main:goal_main')


def update_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    if request.method == "POST":
        goal.category = request.POST['category']
        goal.certify_method = request.POST['certify_method']
        goal.manager = request.user
        goal.name = request.POST['name']
        goal.description = request.POST['description']
        goal.created = timezone.now()
        goal.deadline = request.POST['deadline']
        goal.start_date = request.POST['start_date']
        goal.fee = request.POST['fee']
        goal.member_limit = request.POST['member_limit']
        # 인증 방식이 수치인 경우 인증 기준의 값과 단위를 db에 저장
        if request.POST['certify_method'] == 'figure':
            goal.criteria = request.POST['criteria']
            goal.value = request.POST['value']
            goal.unit = request.POST['unit']
        
        goal.save()
        return redirect('main:goal_detail', goal_id)
    return render(request, 'main/update_goal.html', {'goal':goal})


def delete_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    goal.delete()
    return redirect('main:goal_main')


def participate_goal(request, goal_id):
    goal = Goal.objects.get(pk=goal_id)
    isMember = request.user in goal.member.all()
    if isMember:
        request.user.members.remove(goal)
    else:
        request.user.members.add(goal)
        request.user.profile.cash -= goal.fee
    
    request.user.profile.save()


    return redirect('main:goal_detail', goal_id)