from django.db import models
from user.models import User

class Todo(models.Model):
    """
    Represents a todo item.

    Fields:
    - title (CharField): The title of the todo item (max length: 200 characters).
    - content (TextField): The content or description of the todo item.
    - is_completed (BooleanField): The completion status of the todo item.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    is_completed = models.BooleanField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
