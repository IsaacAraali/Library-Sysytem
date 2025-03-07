# Generated by Django 3.2.12 on 2022-07-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_book_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=10)),
                ('book_name', models.CharField(max_length=50)),
                ('date_borrowed', models.DateTimeField(auto_now_add=True)),
                ('date_return', models.DateTimeField()),
                ('std_id', models.CharField(max_length=10)),
                ('std_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
