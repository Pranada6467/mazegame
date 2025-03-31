from django.shortcuts import render

def index(request):
    context = {'message': 'Welcome to Blockly!'}
    return render(request, 'index.html', context)
