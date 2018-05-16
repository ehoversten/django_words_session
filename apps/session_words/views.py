from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'visits' not in request.session:
        request.session['visits'] = 1
    else:
        request.session['visits'] += 1
    return render(request, 'session_words/index.html')


def process(request):
    print("*"*50)
    print(request.POST)
    if 'words' not in request.session:
        request.session['words'] = [request.POST]

    if 'words' not in request.session:
        request.session['words'] = [request.POST]
    else:
        temp_list = request.session['words']
        temp_list.insert(0, request.POST)
        request.session['words'] = temp_list

    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')
