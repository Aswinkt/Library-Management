from rest_framework import serializers
from .models import Book, User


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField(read_only=True)

    def get_full_name(self, data):
        return data.first_name + "" + data.last_name

    class Meta:

        model = User
        fields = ["user_id","first_name","last_name","full_name","username","type","is_superuser"]


class BookSerializer(serializers.ModelSerializer):

    available_books = serializers.SerializerMethodField(read_only=True)

    def get_available_books(self, data):
        return data.total_books - data.books_taken


    class Meta:

        model = Book
        fields = ['id','title','author','genre','total_books','books_taken','available_books']