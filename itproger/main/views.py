from django.shortcuts import render

def index(request):
    #Список данных в Django
    data = {
        'title': 'Главная страница',
        'values': ['4321','4234','21'],

        'obj':{
            'car': 'Felk',
            'Hello': 'big',
            'age': '20'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
