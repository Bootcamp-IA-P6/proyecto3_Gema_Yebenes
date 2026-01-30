from django.db import models


# Create your models here.
# class ScrapedData(models.Model):
#     title = models.CharField(max_length=200)
#     url = models.URLField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
class ScrapedData(models.Model):
    quote = models.TextField()  # Usamos TextField porque las citas pueden ser largas
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True) # Guardaremos los tags como texto simple
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.created_at}"