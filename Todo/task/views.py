from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import *
from .models import *
from .forms import *

# Create your views here.


#To get the titles from database
def home_view(request):

    query_set = Todo.objects.all()
    cnt=0 #to cnt the no. of incomplete tasks
    check=False
    for i in query_set:
        check=True
        if not i.completed:
            cnt+=1
    # print(cnt)
    my_context={
        'object': query_set,
        'counter': cnt,
        "check": check
    }
    return render(request, 'title-block.html',my_context)




#To get the tasks and also update them or delete them
def link_task_view(request, my_id):

    #If the task does not exist
    try:
        obj = Todo.objects.get(id=my_id)
        form = TodoForm(request.POST or None, instance=obj)
    except ObjectDoesNotExist:
        return redirect('/')

    if form.is_valid():
        form.save()
        if request.method=="POST" and request.POST['pk']=='Delete':
            obj.delete()
        return redirect('/')
    my_context={
        'forms': form
    }

    return render(request, 'task-create.html', my_context)
    



#To create new tasks
def new_task_view(request):

    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    my_context = {
        'forms': form
    }

    return render(request, 'new-task.html', my_context)


#To confirm and delete the task
def confirm_delete_task_view(request, my_id):

    obj = Todo.objects.get(id=my_id)
    obj.delete()
    return redirect('/')