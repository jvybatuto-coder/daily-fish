from django.core.management.base import BaseCommand
from myapp.models import FishCategory

class Command(BaseCommand):
    help = 'Create default fish categories'

    def handle(self, *args, **options):
        default_categories = [
            'Fresh Fish',
            'Saltwater Fish', 
            'Local Fish',
            'Premium Fish',
            'River Fish',
            'Sea Fish',
            'Shellfish',
            'Processed Fish'
        ]

        created_count = 0
        for category_name in default_categories:
            category, created = FishCategory.objects.get_or_create(
                name=category_name,
                defaults={'name': category_name}
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created category: {category_name}')
            else:
                self.stdout.write(f'Category already exists: {category_name}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new categories')
        )
