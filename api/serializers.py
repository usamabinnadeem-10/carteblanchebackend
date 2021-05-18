from rest_framework import serializers
from .models import Todo

# database serialization for the Todo table
class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'

    