
# Create your views here.
from django.shortcuts import render, redirect
from .forms import KullaniciKayitForm, KullaniciGirisForm

from django.contrib.auth import authenticate, login  # Buraya authenticate ve login'ı ekliyoruz




def home(request):
    return render(request, 'home.html')  # 'home.html' şablonunu döndürüyoruz



def kayit(request):
    if request.method == 'POST':
        form = KullaniciKayitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giris')  # Kayıt olduktan sonra giriş sayfasına yönlendir
    else:
        form = KullaniciKayitForm()
    return render(request, 'kayit.html', {'form': form})

def giris2(request):
    if request.method == 'POST':
        form = KullaniciGirisForm(request.POST)
        if form.is_valid():
            return redirect('home')  # Giriş yaptıktan sonra ana sayfaya yönlendir
    else:
        form = KullaniciGirisForm()
    return render(request, 'giris.html', {'form': form})


def giri3(request):
    if request.method == 'POST':
        form = KullaniciGirisForm(request.POST)
        if form.is_valid():
            # Kullanıcıyı authenticate et
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Kullanıcı doğrulandıysa oturumu aç
                login(request, user)
                return redirect('home')  # Giriş yaptıktan sonra ana sayfaya yönlendir
            else:
                # Hatalı kullanıcı adı veya şifre
                form.add_error(None, 'Geçersiz kullanıcı adı veya şifre')
    else:
        form = KullaniciGirisForm()
    return render(request, 'giris.html', {'form': form})





def giris(request):
    if request.method == 'POST':
        form = KullaniciGirisForm(request.POST)
        if form.is_valid():
            # Kullanıcıyı authenticate et
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Kullanıcı doğrulandıysa oturumu aç
                login(request, user)
                return redirect('/admin/')  # Giriş yaptıktan sonra admin sayfasına yönlendir
            else:
                # Hatalı kullanıcı adı veya şifre
                form.add_error(None, 'Geçersiz kullanıcı adı veya şifre')
    else:
        form = KullaniciGirisForm()
    return render(request, 'giris.html', {'form': form})



#-------------------------------- görevler
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Part, Airplane
from .forms import PartForm

# Parçaları Listeleme
def part_list(request):
    parts = Part.objects.all()
    return render(request, 'part_list.html', {'parts': parts})

# Parça Ekleme
def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm()
    return render(request, 'part_form.html', {'form': form})

# Parça Güncelleme
def part_update(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm(instance=part)
    return render(request, 'part_form.html', {'form': form})

# Parça Silme (geri dönüşüm)
def part_delete(request, pk):
    part = get_object_or_404(Part, pk=pk)
    part.delete()
    return redirect('part_list')

