from django.shortcuts import render


def main(request):
    return render(request, 'groups/main.html')


def certify(request):
    return render(request, 'groups/certify.html')
