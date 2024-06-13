from django.urls import reverse_lazy
from django.db import transaction, connection
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
