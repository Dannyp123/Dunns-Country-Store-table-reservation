from django.db import models


# Create your models here.
class TableReservation(models.Model):
    f_name = models.TextField()
    l_name = models.TextField()
    p_number = models.IntegerField()
    num_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    @staticmethod
    def submit_reservation(f_name, l_name, p_number, num_of_people, date,
                           time):
        TableReservation(
            f_name=f_name,
            l_name=l_name,
            p_number=p_number,
            num_of_people=num_of_people,
            date=date,
            time=time).save()
