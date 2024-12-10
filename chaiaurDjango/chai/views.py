from django.shortcuts import render

from .models import ChaiVarity

from django.shortcuts import get_object_or_404


# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})


def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})


def order(request):
    return render(request, 'chai/order.html')
