from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

    
class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%M/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'