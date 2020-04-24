from django.db import models

# Create your models here.

class Header(models.Model):
    image = models.ImageField(
        'Imagem', upload_to='header_img', blank=True, null=True
    )
    tituloGrande = models.CharField('Título Grande', max_length=100)
    whatsapp = models.CharField('Link Whatsapp', max_length=100)

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

    def __str__(self):
        return self.tituloGrande