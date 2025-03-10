# Generated by Django 5.0.2 on 2024-05-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_alter_loknitiresponders_income"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loknitiresponders",
            name="AC_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="PC_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="PS_id",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="age",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="caste",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="education_level",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="election_year",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="gender",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="income",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="occupation",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="religion",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="respondent_no",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="loknitiresponders",
            name="state_name",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
