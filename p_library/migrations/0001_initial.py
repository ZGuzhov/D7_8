# Generated by Django 3.1 on 2020-08-15 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('copy_count', models.SmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.author')),
                ('friend', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='p_library.friend')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.publish')),
            ],
        ),
    ]
