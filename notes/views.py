from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *


# Create your views here.

def Home(request):

    if request.method == 'POST':
        title = request.POST.get('title','')
        description = request.POST.get('description','')
        category = request.POST.get('category','other')

        title = title.strip()
        description = description.strip()

        valid_categories = [choice[0] for choice in Note.CATEGORY_CHOICES]



        if title and description and category in valid_categories:
            Note.objects.create(
                title = title,
                description = description,
                category = category
            )
            messages.success(request,"Note created successfully.")
        else:
            messages.error(request,"Please enter both a title and description.")


        return redirect('home')

    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    notes = Note.objects.all()

    if query:
        notes = notes.filter(title__icontains=query)

    if category_filter:
        notes = notes.filter(category=category_filter)

    total_notes = notes.count()

    context = {
        'notes': notes,
        'total_notes': total_notes,
        'query': query,
        'category_filter': category_filter,
    }

    return render(request, 'notes/home.html', context)


def Edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        category = request.POST.get('category', '')

        valid_categories = [
            choice[0] for choice in Note.CATEGORY_CHOICES
        ]

        if title and description and category in valid_categories:
            note.title = title
            note.description = description
            note.category = category
            note.save()

            messages.success(request, "Note updated successfully.")
            return redirect('home')

        messages.error(
            request,
            "Please enter a title, description, and valid category."
        )

    return render(request, 'notes/edit.html', {'note': note})



def Delete_note(request,note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note,id=note_id)
        note.delete()
    return redirect('home')