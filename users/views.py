from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')
def job_list(request):
    # Dữ liệu ảo để test giao diện
    mock_jobs = [
        {'title': 'Thiết kế Logo', 'budget': '500', 'client_name': 'Hoàng Thiện', 'description': 'Cần tìm người làm logo...'},
        {'title': 'Lập trình Django', 'budget': '2000', 'client_name': 'FreelancerVN', 'description': 'Xây dựng hệ thống backend...'},
    ]
    return render(request, 'jobs_list.html', {'jobs': mock_jobs})

def dashboard(request):
    return render(request, 'dashboard.html')