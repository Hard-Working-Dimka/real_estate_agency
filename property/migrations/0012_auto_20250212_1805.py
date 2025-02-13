# Generated by Django 2.2.24 on 2025-02-12 15:05

from django.db import migrations


def transfer_flats_info(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        owner.flats.set(Flat.objects.filter(owner=owner.owner))
        owner.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0013_auto_20250212_1940'),
    ]

    operations = [
        migrations.RunPython(transfer_flats_info),
    ]
