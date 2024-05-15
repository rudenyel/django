from django.shortcuts import render


def about(request):
    template_name = 'home/about.html'
    return render(request, template_name)
