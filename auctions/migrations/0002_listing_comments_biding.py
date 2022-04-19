# Generated by Django 4.0.3 on 2022-04-19 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('startingBid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('currentPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imageUrl', models.URLField(blank=True)),
                ('category', models.CharField(blank=True, choices=[('FS', 'Fashion'), ('TY', 'Toys'), ('ET', 'Electronics'), ('HM', 'Home')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciption', models.CharField(max_length=128)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Biding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]