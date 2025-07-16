from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.account_number})"


class Transaction(models.Model):
    sender = models.ForeignKey(Customer, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} → {self.receiver.name} : ₹{self.amount}"

