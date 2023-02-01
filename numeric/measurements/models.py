from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from datetime import datetime, date

class Measurements(models.Model):
    Date = models.DateField(auto_now_add=True, verbose_name="Date | Дата")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User | Пользователь")
    Shoulders = models.IntegerField(verbose_name="Shoulders, sm. | Плечи, см.")
    Chest = models.IntegerField(verbose_name="Chest, sm. | Грудь, см.")
    Waist = models.IntegerField(verbose_name="Waist, sm. | Талия, см.")
    Buttocks = models.IntegerField(verbose_name="Buttocks, sm. | Ягодицы, см.")
    Hips = models.IntegerField(verbose_name="Hips, sm. | Бёдра, см.")
    Weight = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Weight, kg. | Вес, кг.", blank=True, null=True)

    class Meta:
        verbose_name = 'Body measurements' # name in admin-panel
        verbose_name_plural = "Body measurements"  # plural
        ordering = ['-Date']

    def get_absolute_url(self):
        return reverse('comparison', kwargs={'comp_slug': self.slug})
