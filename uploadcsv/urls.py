__author__ = 'ranvijay'

from django.conf.urls import patterns, url
from uploadcsv import views

urlpatterns = patterns('',
    url(r'^upload_price_matrix_csv', views.upload_price_matrix_csv),
    url(r'^uploaded_price_matrix_csv_list', views.uploaded_price_matrix_csv_list),
)