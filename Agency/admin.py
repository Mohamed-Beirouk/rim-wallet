from django.contrib import admin
from .models import *

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ("Entitled", "Balance", "CreationDate", "Login", "Password")

admin.site.register(Account, AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("TransactionId", "TransactionDate", "CustomerFullName", "Note", "Currency", "Output", "Input",)

admin.site.register(Transaction, TransactionAdmin)
