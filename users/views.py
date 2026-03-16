from django.shortcuts import render, get_object_or_404
from jobs.models import Job
import requests


def home(request):
    return render(request, 'home/homepage.html')  # nếu bạn đã tổ chức lại template


def fetch_jobs():
    api_url = "https://remotive.com/api/remote-jobs?category=software-dev"
    user_api_url = "https://randomuser.me/api/?results=12"

    try:
        posts_res = requests.get(api_url, timeout=5)
        users_res = requests.get(user_api_url, timeout=5)

        posts = posts_res.json()
        posts = posts.get('jobs', [])[:12]  
        users = users_res.json()['results']

        for i, (post, user) in enumerate(zip(posts, users)):

            Job.objects.update_or_create(
                api_id=post['id'],  # dùng id từ API
                defaults={
                    'title': post['title'][:40].title(),
                    'description': post['description'][:200],
                    'budget': (i + 5) * 100,
                    'client_name': f"{user['name']['first']} {user['name']['last']}",
                    'client_avatar': user['picture']['medium'],
                    'category': "Web Development" if i % 2 == 0 else "Graphic Design",
                }
            )

    except requests.RequestException:
        pass

def job_list(request):
    if Job.objects.count() == 0:
        fetch_jobs()

    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, "jobs/job_detail.html", {"job": job})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')