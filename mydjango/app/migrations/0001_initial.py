# Generated by Django 2.1.2 on 2018-11-06 09:41

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='删除时间')),
            ],
        ),
        migrations.CreateModel(
            name='AccountBank',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('label', models.CharField(max_length=80)),
                ('bsb', models.CharField(max_length=80)),
                ('account_number', models.CharField(max_length=80)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=80)),
                ('swift', models.CharField(max_length=100)),
                ('beneficiary_address', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountTranssction',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('tx_id', models.CharField(max_length=80)),
                ('tx_from', models.CharField(max_length=70)),
                ('tx_to', models.CharField(max_length=70)),
                ('amount', models.BigIntegerField()),
                ('date', models.DateTimeField()),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminRole',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('role_name', models.CharField(max_length=50)),
                ('role_description', models.CharField(max_length=100)),
                ('authority', models.CharField(max_length=100)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('operate_id', models.IntegerField()),
                ('operate_email', models.CharField(max_length=80)),
                ('type', models.IntegerField()),
                ('actions', models.TextField()),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('amount', models.BigIntegerField()),
                ('actual_amount', models.BigIntegerField(default=0)),
                ('bank_txid', models.CharField(max_length=80)),
                ('blcokchain_txid', models.CharField(max_length=80)),
                ('issue_txid', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('order', models.CharField(max_length=16)),
                ('status', models.IntegerField(default=0)),
                ('currency', models.CharField(default='AUD', max_length=80)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Eth',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('eth_label', models.CharField(max_length=80, null=True)),
                ('eth_address', models.CharField(max_length=80, null=True)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('amount', models.BigIntegerField()),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('operate', models.IntegerField()),
                ('is_sms_active', models.BooleanField(default=False)),
                ('is_mail_active', models.BooleanField(default=False)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('phone', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('KYC_status', models.IntegerField(default=2)),
                ('KYC_reason', models.CharField(max_length=80)),
                ('avatar', models.TextField(default=None, null=True)),
                ('is_binding_google', models.BooleanField(default=False)),
                ('is_binding_sms', models.BooleanField(default=False)),
                ('google_secret_key', models.CharField(max_length=80)),
                ('current_amount', models.BigIntegerField()),
                ('frozen', models.BigIntegerField()),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('username', models.CharField(max_length=80, unique=True)),
                ('email', models.EmailField(max_length=80, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('role_type', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_id_verified', models.BooleanField(default=False)),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserKyc',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('given_name', models.CharField(max_length=80)),
                ('family_name', models.CharField(max_length=80)),
                ('birthday', models.DateTimeField()),
                ('kyc_file_type', models.CharField(max_length=80)),
                ('id_document_type', models.CharField(max_length=80)),
                ('file_number', models.CharField(max_length=80)),
                ('expire_date', models.DateTimeField()),
                ('kyc_file', models.TextField()),
                ('document_file', models.TextField()),
                ('country', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('zip_code', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userkyc', to='app.User')),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Base')),
                ('amount', models.BigIntegerField()),
                ('actual_amount', models.BigIntegerField(default=0)),
                ('bank_txid', models.CharField(max_length=80)),
                ('blcokchain_txid', models.CharField(max_length=80)),
                ('redeem_txid', models.CharField(max_length=80)),
                ('status', models.IntegerField(default=0)),
                ('currency', models.CharField(default='AUD', max_length=80)),
                ('bank_label', models.CharField(max_length=80)),
                ('bank_bsb', models.CharField(max_length=80)),
                ('bank_account_number', models.CharField(max_length=80)),
                ('bank_bank_name', models.CharField(max_length=100)),
                ('bank_account_name', models.CharField(max_length=80)),
                ('bank_swift', models.CharField(max_length=100)),
                ('bank_beneficiary_address', models.CharField(max_length=255)),
                ('bank_address', models.CharField(max_length=255)),
                ('remark', models.TextField()),
                ('address', models.CharField(max_length=80)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Profile')),
            ],
            bases=('app.base',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='users',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='app.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='fee',
            name='withdraw_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fee', to='app.Withdraw'),
        ),
        migrations.AddField(
            model_name='eth',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deposit', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='adminrole',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminrole', to='app.User'),
        ),
        migrations.AddField(
            model_name='accountbank',
            name='users',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountbank', to='app.User'),
        ),
    ]