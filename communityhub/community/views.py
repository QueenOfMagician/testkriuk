from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GroupMember,PesanGrup, Group
from django.urls import reverse
from .forms import PesanGrupForm
# Create your views here.

@login_required
def home(request):
    user = request.user
    grm = GroupMember.objects.filter(member=user)
    kosong = "Silahkan Pilih Grup"
    rumah = {"user":user,
             "grm":grm,
             "kosong":kosong}
    
    return render(request, "home.html", rumah)

def gruphome(request, grup_id):
    user = request.user
    group = get_object_or_404(Group, pk=grup_id)
    grm = GroupMember.objects.filter(member=user)
    pesanya =  PesanGrup.objects.filter(grup_id=group) 
    #form Buat PESAN
    if request.method == "POST":
        form = PesanGrupForm(request.POST)
        if form.is_valid():
            pesan_grup = form.save(commit=False)
            pesan_grup.pengirim = user
            pesan_grup.grup_id = group.id
            pesan_grup.save()  # Simpan objek pesan_grup ke database
    else:
        form = PesanGrupForm()
    try:
        home = {"grm":grm,
                "pesanya":pesanya,
                "form":form}
    except:
        pass
    return render(request, "home.html", home)


