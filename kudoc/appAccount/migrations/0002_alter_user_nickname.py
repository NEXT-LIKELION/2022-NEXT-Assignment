from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True),
        ),
    ]
