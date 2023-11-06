from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing and deserializing instances of the Todo model.
    """
    class Meta:
        """
        Meta class for specifying the model and fields to be serialized.
        """
        model = Todo
        fields = ['id', 'title', 'content', 'is_completed']
