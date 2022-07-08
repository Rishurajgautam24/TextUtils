import re
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

def analyzetext(request):
    #Get the text
    djtext = request.POST.get('text','Default')

    #Analyze text
    uppercase = request.POST.get('uppercase','off')
    removespaces = request.POST.get('removespaces','off')
    removelines = request.POST.get('removelines','off')
    removepunc = request.POST.get('removepunc','off')

    #uppercase Analyzer
    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': "UPPERCASE",'analyzed_text': analyzed}
        djtext = analyzed
    #space remover analyzer
    if removespaces == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    #Remove lines analyzer
    if removelines == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    #Remove punchuatuions analyzer
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #if nothing is to do return error
    if(removepunc != "on" and removelines!="on" and removespaces!="on" and uppercase!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'index.html', params)

