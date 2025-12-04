# Generated to fix production deployment issues
# This migration will be faked on production since columns already exist

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_fix_all_missing_fields'),
    ]

    operations = [
        # Empty migration - just to mark the migration state
        # Fields already exist in production database
    ]
