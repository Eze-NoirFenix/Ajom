# Generated by Django 4.1.2 on 2022-11-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_name_alter_product_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='store.category'),
        ),
    ]
