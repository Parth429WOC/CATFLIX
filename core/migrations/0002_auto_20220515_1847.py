# Generated by Django 3.1.5 on 2022-05-15 13:17

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='descripion',
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profiles',
            field=models.ManyToManyField(to='core.Profile'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Kids', 'Kids')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='flyer',
            field=models.ImageField(blank=True, null=True, upload_to='flyers'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('single', 'Single'), ('seasonal', 'Seasonal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
