# Generated by Django 3.2.20 on 2023-08-30 18:20

import apps.store.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titulo')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('short_description', models.TextField(blank=True, verbose_name='Descripcion Corta')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.store.models.category_imagen, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titulo')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('short_description', models.TextField(blank=True, verbose_name='Descripcion Corta')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
                ('sku', models.CharField(max_length=255, verbose_name='SKU')),
                ('specs', models.TextField(blank=True, null=True, verbose_name='Especificaciones')),
                ('stock', models.IntegerField(default=0, verbose_name='STOCK')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio $')),
                ('is_offer', models.BooleanField(default=False, verbose_name='¿Oferta?')),
                ('price_offer', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio Oferta $')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='TC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc', models.DecimalField(decimal_places=2, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Tipo de Cambio',
                'verbose_name_plural': 'Tipo de Cambio',
            },
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titulo')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('short_description', models.TextField(blank=True, verbose_name='Descripcion Corta')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.store.models.category_imagen, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titulo')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('short_description', models.TextField(blank=True, verbose_name='Descripcion Corta')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.store.models.subcategory_imagen, verbose_name='Imagen')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gcategory', to='store.category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Sub Categoria',
                'verbose_name_plural': 'Sub Categorias',
            },
        ),
        migrations.CreateModel(
            name='ProductImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.store.models.product_imagen, verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Actualizado')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product')),
            ],
            options={
                'verbose_name': 'Imagenes de Productos',
                'verbose_name_plural': 'Imagenes de Productos',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Sub Categoria'),
        ),
        migrations.AddField(
            model_name='product',
            name='trademark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.trademark', verbose_name='Marca'),
        ),
    ]
