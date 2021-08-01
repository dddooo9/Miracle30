from django.shortcuts import render


def main(request):
    return render(request, 'groups/main.html')


def certify_image(request):
    return render(request, 'groups/certify_image.html')


def certify_text(request):
    return render(request, 'groups/certify_text.html')


def certify_figure(request):
    return render(request, 'groups/certify_figure.html')