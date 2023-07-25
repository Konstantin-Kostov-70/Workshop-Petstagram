# Generated by Django 4.2.2 on 2023-06-25 10:57
import PetstagramWebsite.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_photo_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='pet_photos', validators=[PetstagramWebsite.photos.validators.validate_file_size]),
        ),
    ]
