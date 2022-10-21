
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agency', '0004_transaction_recu'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='CurrencyName',
            field=models.CharField(default='MRU', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='recu',
            field=models.CharField(default='False', max_length=10),
        ),
    ]
