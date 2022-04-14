from rest_framework import serializers

from .models import Books, LibUser, RentBook, BookCategory


class BookSerializers(serializers.ModelSerializer):
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'


class LibUserSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LibUser
        fields = '__all__'


class RentBookSerializers(serializers.ModelSerializer):

    class Meta:
        model = RentBook
        fields = '__all__'


class BookCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = '__all__'