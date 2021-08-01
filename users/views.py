from django.shortcuts import render


def mypage(request):
    user = request.user
    return render(request, 'users/mypage.html', {'user': user})


def mypage_update(request):
    user = request.user
    if request.method == "POST":
        user.profile.nickname = request.POST.get('nickname')
        user.profile.image = request.FILES.get('image')
        user.save()
        return render(request, 'users/mypage.html', {'user': user})
    return render(request, 'users/mypage_update.html', {'user': user})
