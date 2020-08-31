from django.shortcuts import render
from .models import Books
from .serializers import BooksSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def BooksList(request):
    
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        

