from django.urls import path

from .views import *
#My Urls

urlpatterns = [
    path('',home_view),
    path('task/<str:my_id>/', link_task_view, name="task"),
    path('new-task/', new_task_view, name="new-task"),
    path('delete/<str:my_id>/', confirm_delete_task_view, name="delete")
]
