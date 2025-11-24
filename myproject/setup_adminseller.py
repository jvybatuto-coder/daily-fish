#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User, Group
from myapp.models import UserProfile, Cart

def create_adminseller():
    """Create the adminseller account if it doesn't exist"""
    try:
        # Check if adminseller exists
        if not User.objects.filter(username='adminseller').exists():
            # Create adminseller user
            user = User.objects.create_user(
                username='adminseller',
                email='adminseller@gmail.com',
                password='admin123',
                is_staff=True
            )
            
            # Create related objects
            UserProfile.objects.create(user=user)
            Cart.objects.create(user=user)
            
            # Add to Seller group
            seller_group, _ = Group.objects.get_or_create(name='Seller')
            user.groups.add(seller_group)
            
            print('✅ Created adminseller account successfully')
            print('   Username: adminseller')
            print('   Password: admin123')
            print('   Email: adminseller@gmail.com')
        else:
            print('✅ adminseller account already exists')
            
        # Verify the account
        adminseller = User.objects.get(username='adminseller')
        print(f'   - Is staff: {adminseller.is_staff}')
        print(f'   - Groups: {[group.name for group in adminseller.groups.all()]}')
        print(f'   - Email: {adminseller.email}')
        
    except Exception as e:
        print(f'❌ Error creating adminseller account: {e}')

if __name__ == '__main__':
    create_adminseller()
