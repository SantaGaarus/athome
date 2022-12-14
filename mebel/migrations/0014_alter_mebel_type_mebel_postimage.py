# Generated by Django 4.0.3 on 2022-09-18 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0013_alter_mebel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mebel',
            name='type_mebel',
            field=models.CharField(choices=[('stulya', 'stulya'), ('stoli', 'столы'), ('barnie_stulya', 'barnie_stulya'), ('cresla', 'cresla'), ('crovati', 'crovati'), ('divani', 'divani')], default='стулья', max_length=30),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mebel.mebel')),
            ],
        ),
    ]
