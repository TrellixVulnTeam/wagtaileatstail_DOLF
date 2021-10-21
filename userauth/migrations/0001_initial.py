# Generated by Django 3.1.13 on 2021-10-21 11:27

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('display_name', models.CharField(help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('address1', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='Postal Code')),
                ('city', models.CharField(blank=True, max_length=1024, null=True, verbose_name='City')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone')),
                ('additional_information', models.CharField(blank=True, max_length=4096, null=True, verbose_name='Additional information')),
                ('photo', models.ImageField(default='photos/default-user-avatar.png', upload_to='photos/', verbose_name='Photo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['last_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
