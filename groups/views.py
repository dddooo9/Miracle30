from django.shortcuts import render, get_object_or_404, redirect
from main.models import Goal
from .models import Certify
from datetime import datetime, timedelta
import datetime
from django.utils import timezone


def main(request, goal_id):
    level = []
    total_name = []
    goal = get_object_or_404(Goal, pk=goal_id)
    board = get_board(goal)
    member_count = goal.member.count() + 1
    for date in board['dates']:
        certifies = goal.certifies.filter(created=date)
        count = certifies.count()
        
        if count == 0:
            success_level = 1
        elif count <= member_count * (1/4):
            success_level = 2
        elif count <= member_count * (2/4):
            success_level = 3
        elif count <= member_count * (3/4):
            success_level = 4
        else:
            success_level = 5
        level.append(success_level)
        
        daily_name = []
        for certify in certifies:
            name = certify.user.username
            daily_name.append(name)
        total_name.append(daily_name)
        
    certifiy_list = goal.certifies.all()
    status = get_status(goal)

    context = {
        'goal': goal,
        'dates': board['dates'],
        'member_count': member_count,
        'level': level,
        'name': total_name,
        'certifies': certifiy_list,
        'achievements': board['achievements'],
        'start_days': status['start_days'],
        'success_days': status['success_days'],
        'continuity_days': status['continuity_days'],
    }

    return render(request, 'groups/main.html', context)


def certify(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        user = request.user
        created = timezone.now()
        text = request.POST.get('text')
        image = request.FILES.get('image')
        figure = request.POST.get('figure')
        achievement = True
        if goal.certify_method == 'figure':
            if goal.criteria:  # 이상이어야 성공
                if float(figure) < goal.value:
                    achievement = False
            else:  # 이하여야 성공
                if float(figure) > goal.value:
                    achievement = False
        if achievement:
            user.profile.cash += 20
            user.profile.save()
        Certify.objects.create(goal=goal, user=user, created=created, text=text, image=image, figure=figure, achievement=achievement)
        return redirect('groups:main', goal_id)
    return render(request, 'groups/certify.html', {'goal': goal})


def get_status(goal):   # 시작, 성공, 연속 일수를 리턴하는 함수
    certifies = goal.certifies.all()
    start_days = (datetime.date.today() - goal.start_date).days + 1
    success_days = goal.certifies.filter(achievement=True).count()
    continuity_days = 0
    for i in range(certifies.count()):
        date = datetime.date.today() - timedelta(days=i+1)  # 어제부터 거꾸로 가면서 성공했는지 확인
        certify = goal.certifies.filter(created=date)
        if not certify.first():     # 인증이 없다면 종료
            break
        if not certify.first().achievement:     # 인증이 있으나 실패했으면 종료
            break
        continuity_days += 1    # 성공했으면 연속 일수를 1씩 증가
    res = {
        'start_days': start_days,
        'success_days': success_days,
        'continuity_days': continuity_days,
    }
    return res


def get_board(goal):    # 도장판의 날짜와 성공 여부를 리턴하는 함수
    dates = []
    achievements = []
    for i in range(30):
        date = goal.start_date + timedelta(days=i)
        dates.append(date)
        # 성공 여부
        certify = goal.certifies.filter(created=date)
        if certify:  # 날짜에 해당하는 인증이 있으면
            achievements.append(certify.first().achievement)
        else:  # 인증 안 했으면
            if date < datetime.date.today():    # 과거라면
                achievements.append(False)  # 실천 실패로 처리
            else:   # 미래라면
                achievements.append(None)     # 아무것도 보여주지 않음
    res = {
        'dates': dates,
        'achievements': achievements,
    }
    return res


def group_list(request):
    return render(request, 'groups/group_list.html')

def group_detail(request):
    return render(request, 'groups/group_detail.html')

def make_group(request):
    return render(request, 'groups/make_group.html')
