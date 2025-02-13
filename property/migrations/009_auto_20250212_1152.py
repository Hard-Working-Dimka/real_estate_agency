# Generated by Django 2.2.24 on 2025-02-12 08:52
import phonenumbers
from django.db import migrations


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(flat.owner_pure_phone):
            flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0008_auto_20250212_0206'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers),
    ]
