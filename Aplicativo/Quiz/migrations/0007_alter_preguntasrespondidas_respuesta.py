# Generated by Django 3.2.6 on 2021-08-27 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_preguntasrespondidas_quizuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='respuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.elegirrespuesta'),
        ),
    ]
