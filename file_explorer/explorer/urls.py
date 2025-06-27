from django.urls import path
from . import views
from .views import list_files, upload_file, download_file, delete_file, edit_file, list_files_in_folder, create_folder, \
    copy_file, move_file

urlpatterns = [
    #Ana sayfa için view'ı çağırma
    path('', list_files, name='list_files'),

    #Dosya yükleme için view'ı çağırma
    path('upload/', upload_file, name='upload_file'),

    #Dosya indirme için view'ı çağırma
    path('download/<int:file_id>/', download_file, name='download_file'),

    #Dosya silme için view'ı çağırma
    path('delete/<int:file_id>/', delete_file, name='delete_file'),
    #Dosya düzenleme için view'ı çağırma
    path('edit/<int:file_id>/', edit_file, name='edit_file'),
    
    path('list_files_in_folder/<path:folder>/', list_files_in_folder, name='list_files_in_folder'),

    path('move_file/<int:file_id>/', move_file, name='move_file'),
    path('copy_file/<int:file_id>/', copy_file, name='copy_file'),
    path('create_folder/', views.create_folder, name='create_folder'),
]


