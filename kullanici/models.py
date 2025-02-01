from django.db import models
from django.contrib.auth.models import AbstractUser

# Takımlar (Team)
class Team(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('Kanat Takımı', 'Kanat Takımı'),
        ('Gövde Takımı', 'Gövde Takımı'),
        ('Kuyruk Takımı', 'Kuyruk Takımı'),
        ('Aviyonik Takımı', 'Aviyonik Takımı'),
        ('Montaj Takımı', 'Montaj Takımı'),
    ], unique=True)
    
    def __str__(self):
        return self.name

# Kullanıcı (Kullanici)
class Kullanici(AbstractUser):
    takim = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username

# Uçaklar (Airplane)
class Airplane(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('Akıncı', 'Akıncı'),
        ('Kızılelma', 'Kızılelma'),
    ], unique=True)
    
    def __str__(self):
        return self.name

# Personel (Personnel)
class Personnel(models.Model):
    user = models.OneToOneField(Kullanici, on_delete=models.CASCADE, related_name='personnel')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='personnel')
    
    def __str__(self):
        return self.user.username

# Parçalar (Part)
class Part(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('Kanat', 'Kanat'),
        ('Gövde', 'Gövde'),
        ('Kuyruk', 'Kuyruk'),
        ('Aviyonik', 'Aviyonik'),
    ])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='parts')
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='parts')
    
    def __str__(self):
        return f'{self.name} - {self.airplane.name}'
