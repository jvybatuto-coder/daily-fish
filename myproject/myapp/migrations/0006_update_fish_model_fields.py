# Generated migration for updating Fish model fields

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_fish_seller_sellerprofile'),
    ]

    operations = [
        # Remove old fields
        migrations.RemoveField(
            model_name='fish',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fish',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='fish',
            name='stock_kg',
        ),
        
        # Add new fields
        migrations.AddField(
            model_name='fish',
            name='weight_kg',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='fish',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='fish',
            name='date_purchased',
            field=models.DateField(),
        ),
    ]
