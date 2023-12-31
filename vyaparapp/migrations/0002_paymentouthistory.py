# Generated by Django 4.2.6 on 2023-12-11 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentOutHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('paymentout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.paymentout')),
            ],
        ),
    ]
