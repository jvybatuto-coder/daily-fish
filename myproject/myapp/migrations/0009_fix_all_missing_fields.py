# Generated manually to fix all missing database columns

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_add_description_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='stock_kg',
            field=models.DecimalField(
                decimal_places=2, 
                default=0.00,
                max_digits=10, 
                validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]
            ),
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
