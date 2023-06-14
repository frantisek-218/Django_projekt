from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Vedouci(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno Trenéra', help_text='Zadejte jméno trenéra',
                             error_messages={'blank': 'Jméno trenéra musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení trenéra', help_text='Zadejte příjmení trenéra',
                                error_messages={'blank': 'Příjmení trenéra musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    biografie = models.TextField(blank=True, verbose_name='Životopis')
    fotografie = models.ImageField(upload_to="./media", height_field=None, width_field=None, max_length=100,  blank = True,null=True)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Trenér'
        verbose_name_plural = 'Trenéři'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'
    
class Liga(models.Model):
    liga = models.CharField(max_length=80, verbose_name='Název ligy', help_text='Zadejte název ligy',
                             error_messages={'blank': 'Název ligy musí být vyplněn'})
    zalozeni = models.IntegerField(verbose_name='Rok zalozeni',help_text='Zadejte rok založení ligy',default="1900",
        validators=[
            MinValueValidator(1898),  # Minimum allowed year
            MaxValueValidator(2023),  # Maximum allowed year
        ]
    )
    class Meta:
        ordering = ['liga']
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligy'

    def __str__(self):
        return f'{self.liga}-{self.zalozeni}'


class Klub(models.Model):
    nazev = models.CharField(max_length=80, verbose_name='Název Klubu', help_text='Zadejte název Klubu',
                             error_messages={'blank': 'Název Klubu musí být vyplněn'})
    zalozeni = models.DateField(blank=True, null=True, verbose_name='Datum založení klubu')
    zeme = models.CharField(max_length=80,default="unknown", verbose_name='Název Země', help_text='Zadejte název země odkud Klub pochází',
                             error_messages={'blank': 'Název země musí být vyplněn'})
    #fotografie = models.ImageField(upload_to='kluby_fotky', verbose_name='Fotografie')
    trener = models.ManyToManyField(Vedouci)
    liga = models.ManyToManyField(Liga)
    foto_klubu = models.ImageField(upload_to="kluby", height_field=None, width_field=None, max_length=100,  blank = True,null=True)
    HODNOCENI = (
        (0, 'Liga Mistrů'),
        (1, 'Evropská Liga'),
        (2, 'Evropská Konferční Liga'),
        (3, "Nekvalifikován")
    )
    turnaje = models.PositiveSmallIntegerField(choices=HODNOCENI,
                                                 verbose_name='Hodnocení',
                                                 default=3)

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Klub'
        verbose_name_plural = 'Kluby'

    def __str__(self):
        return self.nazev



     
# Create your models here.
