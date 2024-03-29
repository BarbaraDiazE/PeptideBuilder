# Generated by Django 2.1 on 2020-01-22 17:47

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pca_fp', multiselectfield.db.fields.MultiSelectField(choices=[('MACCS Keys', 'MACCS Keys'), ('ECFP 4', 'ECFP 4'), ('ECFP 6', 'ECFP6'), ('Topological', 'Topological'), ('Atom Pair', 'Atom Pair')], max_length=46, verbose_name='Fingerprint')),
                ('tsne_fp', multiselectfield.db.fields.MultiSelectField(choices=[('MACCS Keys', 'MACCS Keys'), ('ECFP 4', 'ECFP 4'), ('ECFP 6', 'ECFP6'), ('Topological', 'Topological'), ('Atom Pair', 'Atom Pair')], max_length=46, verbose_name='Fingerprint')),
            ],
        ),
    ]
