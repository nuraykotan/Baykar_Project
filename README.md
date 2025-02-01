# Baykar_Project
Personel Giriş Sistemi / Django / PostegroSQL

Kullanılan Teknolojiler
Backend: Django 
Database: PostgreSQL
Frontend: HTML, CSS
Versiyon Kontrol: Git & GitHub

⚙ Kurulum
1-Projeyi Klonla:
git clone https://github.com/nuraykotan/Baykar_Project.git
cd Baykar_Project


2-Sanal Ortamı Oluştur ve Aktifleştir:
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/macOS için:
source venv/bin/activate


3-Gerekli Bağımlılıkları Yükle:


4-PostgreSQL Bağlantısını Yapılandır:
settings.py dosyasında PostgreSQL bağlantısını güncelle:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'veritabani_adi',
        'USER': 'kullanici_adi',
        'PASSWORD': 'sifre',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


5-Veritabanını Güncelle:
python manage.py migrate
python manage.py createsuperuser  # Yönetici hesabı oluştur


6-Projeyi Çalıştır:
python manage.py runserver

