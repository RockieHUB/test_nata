# Generated by Django 5.1 on 2024-09-03 04:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_alter_pelatihan_harga'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pelatihan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pelatihan')),
            ],
            options={
                'unique_together': {('akun', 'pelatihan')},
            },
        ),
    ]
