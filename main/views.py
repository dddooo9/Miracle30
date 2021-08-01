from django.shortcuts import render


def main_login(request):
    return render(request, 'main/main_login.html')


def main_logout(request):
    return render(request, 'main/main_logout.html')


def goal_main(request):
    return render(request, 'main/goal_main.html')


def add_goal(request):
    return render(request, 'main/add_goal.html')