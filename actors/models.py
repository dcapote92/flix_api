from django.db import models

NATIONALITY_CHOICES = (
    ('BRAZIL', 'Brasil'),
    ('USA', 'Estados Unidos'),
    ('AUS', 'Australia'),
    ('GBR', 'Gran Bretanha'),
    ('CAN', 'Canada'),
    ('ESP', 'Espanha'),
    ('RSA', 'Africa do Sul'),
    ('USA-GBR', 'Estados Unidos - Gran Bretanha'),
    ('GBR-AUS', 'Gran Bretanha - Australia'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
