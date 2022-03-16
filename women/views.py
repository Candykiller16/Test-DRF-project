from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women
from .serializers import WomenSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Women.objects.all()
#         return Women.objects.filter(pk=pk)

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'title': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesn't exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object doesn't exist"})
#
#         return Response({"post": "deleted post"+str(pk)})
