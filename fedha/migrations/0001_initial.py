# Generated by Django 3.2.9 on 2021-12-30 16:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=200)),
                ('neighbourhood_location', models.CharField(max_length=200)),
                ('neighbourhood_description', models.TextField(blank=True, max_length=500)),
                ('neighbourhood_photo', cloudinary.models.CloudinaryField(default='photo', max_length=255, verbose_name='photo')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fedha.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Security'), ('2', 'Health Emergency'), ('3', 'Entertainment'), ('4', 'Fire Breakouts'), ('5', 'Playground'), ('6', 'Death'), ('7', 'Gym')], max_length=120)),
                ('title', models.CharField(max_length=100, null=True)),
                ('post', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_post', to='fedha.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='fedha.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_email', models.CharField(max_length=150)),
                ('business_description', models.TextField()),
                ('neighbourhood_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='fedha.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_owner', to='fedha.profile')),
            ],
        ),
    ]
