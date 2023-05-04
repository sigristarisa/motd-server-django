# Generated by Django 4.2 on 2023-05-04 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Mayonnaise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ingredient', models.CharField(max_length=20)),
                ('portion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Combination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mayonnaise.dish')),
                ('mayonnaise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mayonnaise.mayonnaise')),
            ],
        ),
    ]
