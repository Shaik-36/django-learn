from django.shortcuts import render

from .models import ChaiVarity, Store

from django.shortcuts import get_object_or_404

from .forms import ChaiVarityForm


# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})


def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})


def order(request):
    return render(request, 'chai/order.html')

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']

            # Match the filtered chai_varity from the whole model store -> chai_varities (Models->Store->chai_varities)
            stores = Store.objects.filter(chai_varities=chai_variety)             # From Models -> Stores Method -> variable chai_varities
    else:
            form= ChaiVarityForm()

    # Send the stores and form that we created in this function
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form} )
