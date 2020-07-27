# Generated by Django 3.0.8 on 2020-07-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachamama', '0006_auto_20200724_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='basevendasrealizadas',
            name='valor_cmv_total_2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basevendasrealizadas',
            name='valor_cmv_unit_2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basevendasrealizadas',
            name='cliente_faturamento_2',
            field=models.CharField(max_length=1000),
        ),
    ]