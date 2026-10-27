from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('edit/<int:note_id>',views.Edit_note,name='edit_note'),
    path('delete/<int:note_id>',views.Delete_note,name='delete_note'),
]