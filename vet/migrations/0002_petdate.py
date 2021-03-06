# Generated by Django 3.2.5 on 2021-08-04 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('type', models.CharField(choices=[('esthetic', 'Esthetic'), ('disease', 'Disease'), ('vaccine', 'Vaccine'), ('deworming', 'Deworming')], default='esthetic', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dates', to='vet.pet')),
            ],
        ),
    ]
