from django.shortcuts import render
from rest_framework.response import Response
from app.serializers import *
from app.models import *
from rest_framework.views import APIView
# Create your views here.
class productcls(APIView):
    def get(self,request,pid):
        # pqs=product.objects.all()
        # pjd=productmodelserializer(pqs,many=True)
        pqs=product.objects.get(pid=pid)
        pjd=productmodelserializer(pqs)
        return Response(pjd.data)
    
    def post(self,request):
        ujsd=request.data
        pd=productmodelserializer(data=ujsd)
        if pd.is_valid():
            pd.save()

            return Response({'message':'Product is Created'})
        else:
            return Response({'Failed':'Product is not created'})
            



    def put(self,request,pid):
        ujsd=request.data
        po=product.objects.get(pid=ujsd['pid'])
        pd=productmodelserializer(po,data=ujsd)
        if pd.is_valid():
            pd.save()
            return Response({'messsage':'product is updated'})
        else:

            return Response({'failed':'product is not updated'})
        

    def patch(self,request,pid):
        ujsd=request.data
        po=product.objects.get(pid=ujsd['pid'])
        pd=productmodelserializer(po,data=ujsd,partial=True)
        if pd.is_valid():
            pd.save()

            return Response({'message':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})
        


    def delete(self,request,pid):
        po=product.objects.get(pid=pid)
        po.delete()
        return Response({'message':'Product is Deleted'})
