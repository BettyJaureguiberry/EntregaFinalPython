from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=200)                 # ✅ CharField 1
    subtitle = models.CharField(max_length=300)              # ✅ CharField 2
    content = RichTextField()                                # ✅ Texto enriquecido con CKEditor
    image = models.ImageField(upload_to='pages/images/')     # ✅ Imagen
    date = models.DateField(auto_now_add=True)               # ✅ Fecha
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title