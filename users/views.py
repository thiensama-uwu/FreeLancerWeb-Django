from django.shortcuts import render
import requests


def home(request):
    return render(request, 'home/homepage.html')  # nếu bạn đã tổ chức lại template


def fetch_jobs():
    api_url = "https://jsonplaceholder.typicode.com/posts?_limit=12"
    user_api_url = "https://randomuser.me/api/?results=12"

    jobs_data = []

    try:
        posts_res = requests.get(api_url, timeout=5)
        users_res = requests.get(user_api_url, timeout=5)

        posts_res.raise_for_status()
        users_res.raise_for_status()

        posts = posts_res.json()
        users = users_res.json()['results']

        for i, (post, user) in enumerate(zip(posts, users)):
            jobs_data.append({
                'title': post['title'][:40].title(),
                'description': post['body'][:150] + "...",
                'budget': (i + 5) * 100,
                'client_name': f"{user['name']['first']} {user['name']['last']}",
                'client_avatar': user['picture']['medium'],
                'category': "Web Development" if i % 2 == 0 else "Graphic Design"
            })

    except requests.RequestException as e:
        print(f"Lỗi gọi API: {e}")
        jobs_data = [{
            'title': 'Công việc mẫu',
            'description': 'Dữ liệu dự phòng',
            'budget': 500,
            'client_name': 'Admin',
            'client_avatar': '',
            'category': 'General'
        }]

    return jobs_data


def job_list(request):
    jobs = fetch_jobs()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')