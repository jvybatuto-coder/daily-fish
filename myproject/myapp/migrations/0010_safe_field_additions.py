# Generated migration to safely handle existing fields in production

from django.db import migrations, models
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_fix_all_missing_fields'),
    ]

    operations = [
        # These operations will be skipped if fields already exist
        migrations.AddField(
            model_name='fish',
            name='stock_kg',
            field=models.DecimalField(
                decimal_places=2, 
                default=0.00,
                max_digits=10, 
                validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fish',
            name='weight_kg',
            field=models.DecimalField(
                decimal_places=2, 
                default=0.00,
                max_digits=10, 
                help_text='Weight of fish in kilograms',
                validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fish',
            name='total_price',
            field=models.DecimalField(
                decimal_places=2, 
                default=0.00,
                max_digits=10, 
                help_text='Total price for this fish',
                validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fish',
            name='date_purchased',
            field=models.DateField(
                blank=True, 
                help_text='Date when fish was purchased to track freshness', 
                null=True
            ),
        ),
        migrations.AddField(
            model_name='fish',
            name='image_url',
            field=models.URLField(
                blank=True, 
                help_text='External image URL if no local image'
            ),
        ),
        migrations.AddField(
            model_name='fish',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='fish',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
