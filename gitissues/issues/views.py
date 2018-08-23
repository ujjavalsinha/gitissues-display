from django.shortcuts import render
import requests
from django.views.generic import CreateView
from issues.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'

def IssueList(request):
    url = 'https://api.github.com/repos/crashlytics/secureudid/issues'
    r = requests.get(url)
    issue = r.json()
    all_issues=[]

    for i in range(len(issue)):

        issues_list={
        'title':issue[i]["title"],
        'name':issue[i]["user"]["login"],
        'id':issue[i]["user"]["id"],
        'avatar':issue[i]["user"]["avatar_url"],
        'number':issue[i]["number"],

        'body':issue[i]["body"]
        }
        all_issues.append(issues_list)
    context={'all_issues':all_issues}
    return render(request,'issues/issues_list.html',context)

def detail(request,id):

    url = 'https://api.github.com/repos/crashlytics/secureudid/issues/{}'
    r = requests.get(url.format(id))
    issue=r.json()
    comments=requests.get(issue["comments_url"]).json()
    allcomments=[]
    for i in range(len(comments)):
        comment_list={
        'body':comments[i]["body"],
        'name':comments[i]["user"]["login"]
        }
        allcomments.append(comment_list)

    context={
    'avatar':issue["user"]["avatar_url"],
    'title':issue["title"],
    'name':issue["user"]["login"],
    'body':issue["body"],
    'allcomments':allcomments,
    }
    return render(request,'issues/issues_detail.html',context)
