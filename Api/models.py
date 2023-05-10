import uuid
from django.db import models


class BooksApiModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=15, decimal_places=12)
    isbn = models.CharField(max_length=255, unique=True)


    class Meta:
        db_table = "books"
        ordering = ['-id']

    def __str__(self) -> str:
            return self.title   
