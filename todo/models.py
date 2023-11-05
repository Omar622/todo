from django.db import models


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
