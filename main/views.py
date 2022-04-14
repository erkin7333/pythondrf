from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView,\
    RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Books, LibUser, RentBook, BookCategory
from .pagination import CustomPagination
from .serializers import BookSerializers, LibUserSerializers, RentBookSerializers, BookCategorySerializers


# class BookViewsets(viewsets.ModelViewSet):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers

# Viewsetda list amali bilan bazadagi malumotni o'qish
class BookViewsets(viewsets.ViewSet):
    pagination_class = CustomPagination
    def list(self, request):
        queryset = Books.objects.all()
        serializers = BookSerializers(queryset, many=True)
        return Response(serializers.data)

    # Viewsetda post amali yordamida bazaga malumot qo'shish usuli
    def post(self, request):
        serializers = BookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LibUserViewSets(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializers
    pagination_class = CustomPagination



class RentBookViewSets(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializers
    pagination_class = CustomPagination

# GET Amalii bajarldi
# ListView yordamidan bazadagi Kitoblar kategoriyalarni ko'rish uchun ishlatim
class BookCategoryListView(ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers
    pagination_class = CustomPagination

# POST Amalii bajarildi
# CreateView yordamida Bazaga Kitob Kategoryalarinii kiritish usuli
class BookCategoryCreatView(CreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers
    pagination_class = CustomPagination


# GET va POST amalarii bir vaqt o'zida ishlatildi
# ListCreateAPIView yordamida Bazadagi kitoblari kategorilarini ko'rish va kategoriya qo'shish usuli
class BookCategoryListCreateView(ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers
    pagination_class = CustomPagination


# GET Amali
# RetrieveAPIView amali yordamida bazadagi malumotlarni har birinii aloxida ko'rish uchun ishlatiladi
class BookCategoryRetrivewView(RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


# PUT Amali
class BookCategoryUpdateView(UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


# GET va PUT Amalarini bir vaqt ishida bajarish
# RetrieveUpdateAPIView Yordamida bitta obyekti ustida ikkita amal bajarish
class BookCategoryRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


# DELETE Amalii
class BookCategoryDeleteView(DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


