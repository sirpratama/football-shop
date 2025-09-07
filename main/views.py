from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406453556',
        'name': 'Muhammad Rafi Nazir Pratama',
        'class': 'KKI'
    }

    return render(request, "main.html", context)