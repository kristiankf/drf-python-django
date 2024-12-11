# from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST", "GET"])
def api_home(request, *args, **kwargs):
    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            data = serializer.data
            return Response(data)