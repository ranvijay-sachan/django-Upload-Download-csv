import csv
from django.http import HttpResponse
from django.shortcuts import render_to_response
from uploadcsv.forms import UploadCsvForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from uploadcsv.models import UploadCsv

def upload_price_matrix_csv(request):
    if request.method == 'POST':
            form = UploadCsvForm(request.POST, request.FILES)
            if form.is_valid():
                csv_form = UploadCsv(title=request.POST["title"],
                                     upload_file=request.FILES['upload_file'],
                                     city=request.POST["city"])
                csv_form.save()
                return HttpResponseRedirect('/update_price_matrix/uploaded_price_matrix_csv_list')
            else:
                return HttpResponse('Invalid image')
    else:
        form = UploadCsvForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
    return render_to_response('csv/upload_price_matrix_csv.html',  args)


def uploaded_price_matrix_csv_list(request):
    return render_to_response('csv/uploaded_price_matrix_csv_list.html', {'csvlist': UploadCsv.objects.all()})
