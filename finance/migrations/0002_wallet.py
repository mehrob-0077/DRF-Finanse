from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def create_wallets(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    Wallet = apps.get_model('finance', 'Wallet')
    Transaction = apps.get_model('finance', 'Transaction')
    db = schema_editor.connection.alias
    for user in User.objects.using(db).all():
        wallet, _ = Wallet.objects.using(db).get_or_create(user_id=user.pk)
        Transaction.objects.using(db).filter(user_id=user.pk).update(wallet_id=wallet.pk)


class Migration(migrations.Migration):
    dependencies = [('finance', '0001_initial')]

    operations = [
        migrations.CreateModel(name='Wallet', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('name', models.CharField(default='My wallet', max_length=100)),
            ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
        ]),
        migrations.AddField(model_name='transaction', name='wallet', field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.wallet')),
        migrations.RunPython(create_wallets, migrations.RunPython.noop),
        migrations.AlterField(model_name='transaction', name='wallet', field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='finance.wallet')),
        migrations.RemoveField(model_name='transaction', name='user'),
        migrations.RemoveField(model_name='transaction', name='category'),
        migrations.DeleteModel(name='Category'),
    ]
