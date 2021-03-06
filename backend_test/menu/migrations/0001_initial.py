# Generated by Django 2.0.9 on 2018-11-29 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 'ingredients',
            },
        ),
        migrations.CreateModel(
            name='IngredientException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ManyToManyField(to='menu.Ingredient', verbose_name='ingredients')),
            ],
            options={
                'verbose_name': 'exception',
                'verbose_name_plural': 'exceptions',
            },
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
            ],
            options={
                'verbose_name': 'lunch',
                'verbose_name_plural': 'lunches',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('lunches', models.ManyToManyField(to='menu.Lunch', verbose_name='lunches')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Lunch', verbose_name='lunch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
                ('recipe', models.ManyToManyField(to='menu.Ingredient', verbose_name='recipe')),
            ],
            options={
                'verbose_name': 'preparation',
                'verbose_name_plural': 'preparations',
            },
        ),
        migrations.AddField(
            model_name='lunch',
            name='preparations',
            field=models.ManyToManyField(to='menu.Preparation', verbose_name='preparations'),
        ),
        migrations.AddField(
            model_name='ingredientexception',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Order', verbose_name='order'),
        ),
        migrations.AddField(
            model_name='ingredientexception',
            name='preparation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Preparation', verbose_name='preparation'),
        ),
    ]
