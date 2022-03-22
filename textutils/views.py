# I have created this file - Shrikant
from django.http import HttpResponse
from django.shortcuts import render
# Code for video no 6
# def index(request):
#     return HttpResponse('''<h1>Prakrut</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k">Django Code with Shri</a>''')
#
# def about(request):
#     return HttpResponse("About")

# Code for video no 7
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home page")

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("Punc")

def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove(request):
    return HttpResponse("Remove space")

def charcount(request):
    return HttpResponse("Charcount")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Newline Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + djtext[index]
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if charactercounter == "on":
        analyzed = ""
        counter = 0
        for char in djtext:
            counter = counter + 1
        analyzed = f"Characters in string are: {counter}"
        params = {'purpose': 'Count characters in string', 'analyzed_text': analyzed}
        if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter == "on"):
            return  HttpResponse("Error")

    return render(request, 'analyze.html', params)