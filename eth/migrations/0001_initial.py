# Generated by Django 2.1.4 on 2018-12-26 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('hash', models.CharField(max_length=255)),
                ('parent_hash', models.CharField(max_length=255)),
                ('nonce', models.IntegerField()),
                ('size', models.IntegerField()),
                ('difficulty', models.CharField(max_length=255)),
                ('total_difficulty', models.CharField(max_length=255)),
                ('gas_limit', models.DecimalField(decimal_places=18, max_digits=36)),
                ('gas_used', models.DecimalField(decimal_places=18, max_digits=36)),
                ('author', models.CharField(max_length=255)),
                ('miner', models.CharField(max_length=128)),
                ('extra_data', models.CharField(max_length=1024)),
                ('logs_bloom', models.CharField(max_length=2048)),
                ('mix_hash', models.CharField(max_length=255)),
                ('receipts_root', models.CharField(max_length=255)),
                ('seal_fields', models.CharField(max_length=1024)),
                ('sha3_uncles', models.CharField(max_length=255)),
                ('state_root', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('hash', models.CharField(max_length=255)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=255)),
                ('from_address', models.CharField(max_length=255)),
                ('to_address', models.CharField(max_length=255)),
                ('gas', models.DecimalField(decimal_places=18, max_digits=36)),
                ('gas_price', models.DecimalField(decimal_places=18, max_digits=36)),
                ('chain_id', models.CharField(max_length=4)),
                ('condition', models.CharField(max_length=255, null=True)),
                ('creates', models.CharField(max_length=255, null=True)),
                ('input', models.CharField(max_length=255)),
                ('nonce', models.IntegerField()),
                ('public_key', models.CharField(max_length=1024)),
                ('r', models.CharField(max_length=255)),
                ('raw', models.CharField(max_length=2048)),
                ('s', models.CharField(max_length=4096)),
                ('standard_v', models.CharField(max_length=4)),
                ('transaction_index', models.CharField(max_length=4)),
                ('v', models.CharField(max_length=8)),
                ('value', models.CharField(max_length=32)),
                ('block_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ex.eth.Blocks')),
            ],
        ),
    ]
