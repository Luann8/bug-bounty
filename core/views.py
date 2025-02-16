from django.shortcuts import render

def index(request):
    return render(request, 'bug_bounty/index.html')