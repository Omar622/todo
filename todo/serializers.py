from rest_framework import serializers
from .models import Todo
from user.models import User


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing and deserializing instances of the Todo model.
    """

    class Meta:
        """
        Meta class for specifying the model and fields to be serialized.
        """
        model = Todo
        fields = ['id', 'user', 'title', 'content',
                  'is_completed', 'created_at', 'updated_at']
        extra_kwargs = {
            'user': {'write_only': True}
        }
