# Generated by Django 3.1.2 on 2020-11-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Category',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=200)),
        #         ('image', models.ImageField(blank=True, null=True, upload_to='')),
        #         ('description', models.TextField(blank=True)),
        #     ],
        #     options={
        #         'verbose_name': 'Category',
        #         'verbose_name_plural': 'Categories',
        #     },
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='category',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.category'),
        #     preserve_default=False,
        # ),
    ]