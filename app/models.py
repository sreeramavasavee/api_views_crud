from django.db import models

# Create your models here.
class product_categories(models.Model):
    cname=models.CharField(max_length=50)
    cid=models.PositiveIntegerField()
    def _str__(self):
        return self.cname


class product(models.Model):
    cname=models.ForeignKey(product_categories,on_delete=models.CASCADE)
    pid=models.PositiveBigIntegerField()
    pname=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.pname
    


