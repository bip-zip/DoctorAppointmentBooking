from django.db import models

doctor_category=(('pathologist','Pathologist'),
                ('psychiatrist','Psychiatrist'),
                ('surgeon','Surgeon'),
                ('anesthesiologist','Anesthesilogist'),
                ('neurologist','Neurologist'),
                ('pulmonologist','Pulmonologist'),
                ('dermatologist','Dermatologist'),
                ('cardiologist','Cardiologist'))



class Doctor(models.Model):
    doctorName=models.CharField(max_length=200)
    category= models.CharField(max_length=200,choices=doctor_category )
    age=models.IntegerField()
    number=models.CharField(max_length=12)
    picture=models.ImageField(upload_to="doctor_profile")
    time=models.CharField(max_length=12)

    def __str__(self):
        return str(self.doctorName)

    @property
    def profileImg(self):
        try:
            url= self.picture.url
        except:
            url=""
        return url









