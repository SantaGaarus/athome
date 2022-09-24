# Generated by Django 4.0.3 on 2022-09-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0022_stoli_nojki_stoli_stoleshnitsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='crovati',
            name='SRegulVisot',
            field=models.BooleanField(default=1, verbose_name='Глянец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='barStul',
            field=models.BooleanField(default=1, verbose_name='С подъемным механизмом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='description',
            field=models.CharField(default=1, max_length=200, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='dlina_width',
            field=models.IntegerField(default=1, verbose_name='Длина общая:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='height_izg',
            field=models.IntegerField(default=1, verbose_name='Высота изголовь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='image1',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='image2',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='image3',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='image4',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='image5',
            field=models.ImageField(default=1, upload_to='mebel/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='nojki',
            field=models.CharField(default=1, max_length=200, verbose_name='Ножки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='obivka',
            field=models.CharField(default=1, max_length=200, verbose_name='Обивка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='polubarStul',
            field=models.BooleanField(default=1, verbose_name='Без подъемного механизма'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='spal_mest',
            field=models.CharField(default=1, max_length=200, verbose_name='Спальное место:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='width',
            field=models.IntegerField(default=1, verbose_name='Ширина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crovati',
            name='width_izn',
            field=models.IntegerField(default=1, verbose_name='Высота изножья'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='Krug',
            field=models.BooleanField(default=1, verbose_name='Круглые столы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='Oval',
            field=models.BooleanField(default=1, verbose_name='Овальные столы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='PryamoUg',
            field=models.BooleanField(default=1, verbose_name='Прямоугольные столы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='SKeramPok',
            field=models.BooleanField(default=1, verbose_name='С керамическим покрытием'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='SoStecl',
            field=models.BooleanField(default=1, verbose_name='Со стеклом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='Stul_transformer',
            field=models.BooleanField(default=1, verbose_name='Стол-трансформер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='description',
            field=models.TextField(default=1, max_length=10000, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stoli',
            name='raskladnoy',
            field=models.BooleanField(default=1, verbose_name='Раскладной'),
            preserve_default=False,
        ),
    ]