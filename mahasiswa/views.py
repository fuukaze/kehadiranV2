from django.shortcuts import render
from pengurus.models import Kehadiran

# Create your views here.
def index(request):
    # Fetch the latest data from the Kehadiran model
    latest_data = Kehadiran.objects.order_by('-id')[:1]

    context = {'latest_data': latest_data}
    
    return render(request, 'mahasiswa/index.html', context)
