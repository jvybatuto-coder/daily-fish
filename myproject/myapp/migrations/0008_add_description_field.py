# Generated manually to fix missing description column

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_fish_date_purchased_alter_fish_total_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
