from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render
from app.data import BREAKFAST
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
class AdminHome(View):
    def get(self, request):
        return render(request, "admin-home.html",
                      {"admin_home": models.TableReservation.objects.all()})


class HuntingFishing(View):
    def get(self, request):
        return render(request, "hunting-fishing.html")


class BeerTobacco(View):
    def get(self, request):
        return render(request, "beer-tobacco.html")


class Menu(View):
    def get(self, request):
        return render(request, "menu.html", {"BREAKFAST": BREAKFAST})


class MakeReservation(View):
    def get(self, request):
        return render(request, "reservation-form.html",
                      {"reservation_form": forms.TableReservationForm()})

    def post(self, request):
        form = forms.TableReservationForm(data=request.POST)
        if form.is_valid():
            f_name = form.cleaned_data["f_name"]
            l_name = form.cleaned_data["l_name"]
            p_number = form.cleaned_data["p_number"]
            num_of_people = form.cleaned_data["num_of_people"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            email = form.cleaned_data["email"]

            models.TableReservation.submit_reservation(
                f_name, l_name, p_number, num_of_people, date, time, email)

            return redirect("user-home")

        else:
            return render(request, "reservation-form.html",
                          {"reservation_form": form})


class TableReservation(View):
    def get(self, request):
        return render(request, "reservation-form.html",
                      {"reserve": models.TableReservation.objects.all()})


class ReservedTables(View):
    def get(self, request):
        return render(request, "reservered-tables.html",
                      {"reserved": models.TableReservation.objects.all()})


class ReservedTable(View):
    def get(self, request, id):
        return render(
            request, "reserved-table.html",
            {"reserved_table": models.TableReservation.objects.get(id=id)})


class UserHome(View):
    def get(self, request):
        return render(request, "user-home.html",
                      {"user_admin": models.TableReservation.objects.all()})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You can now login")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "profile.html")
