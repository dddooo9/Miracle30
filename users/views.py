from django.db.models import manager
from django.shortcuts import redirect, render
from main.models import Goal

def mypage(request):
    user = request.user
    goals = Goal.objects.all()

    my_goal = []
    participate_goal = []

    for goal in goals:
        if goal.manager == user:
            my_goal.append(goal)
        elif user in goal.member.all():
            participate_goal.append(goal)
    
    context = {
        'user':user,
        'my_goal':my_goal,
        'participate_goal':participate_goal
    }
    return render(request, 'users/mypage.html', context)


def mypage_update(request):
    user = request.user
    if request.method == "POST":
        user.profile.nickname = request.POST.get('nickname')
        user.profile.image = request.FILES.get('image')
        user.save()
        return redirect('users:mypage')
    return render(request, 'users/mypage_update.html', {'user': user})



