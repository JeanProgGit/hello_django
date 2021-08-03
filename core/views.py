from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello world {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>{} + {} = {} </h1>'.format(num1, num2, soma))

def sub(request, num1, num2):
    sub = num1 - num2
    return HttpResponse('<h1>{} - {} = {} </h1>'.format(num1, num2, sub))

def mult(request, num1, num2):
    mult = num1 * num2
    return HttpResponse('<h1>{} * {} = {} </h1>'.format(num1, num2, mult))

def div(request, num1, num2):
    div = num1 / num2
    return HttpResponse('<h1>{} / {} = {} </h1>'.format(num1, num2, div))

