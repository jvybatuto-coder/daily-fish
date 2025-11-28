# Generated migration for updating Fish model fields

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_fish_seller_sellerprofile'),
    ]

    operations = [
        # Add new fields with default values for existing records
        migrations.AddField(
            model_name='fish',
            name='weight_kg',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='fish',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AddField(
            model_name='fish',
            name='date_purchased',
            field=models.DateField(default='2025-01-01'),
        ),
    ]
