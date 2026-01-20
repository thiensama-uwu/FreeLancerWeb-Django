from django.shortcuts import render

# Đây là hàm bị thiếu khiến lỗi xảy ra
def home(request):
    return render(request, 'homepage.html')