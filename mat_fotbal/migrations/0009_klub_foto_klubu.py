# Generated by Django 4.2.1 on 2023-05-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mat_fotbal', '0008_vedouci_fotografie'),
    ]

    operations = [
        migrations.AddField(
            model_name='klub',
            name='foto_klubu',
            field=models.ImageField(blank=True, null=True, upload_to='./media'),
        ),
    ]
