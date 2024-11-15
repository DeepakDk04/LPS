# Generated by Django 5.1.3 on 2024-11-12 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('IsPurchValApplicable', models.BooleanField(default=False)),
                ('percentFromPurchVal', models.FloatField(blank=True, null=True)),
                ('IsPreSetPointApplicable', models.BooleanField(default=False)),
                ('preSetPoint', models.IntegerField(blank=True, null=True)),
                ('IsPointCap', models.BooleanField(default=False)),
                ('capPerOrder', models.IntegerField(blank=True, null=True)),
                ('capPerConsumer', models.IntegerField(blank=True, null=True)),
                ('capPerTimeline', models.IntegerField(blank=True, null=True)),
                ('capTimeLine', models.DateField(blank=True, null=True)),
                ('campaignName', models.CharField(default='New Campaign', max_length=20)),
                ('campaignStartDate', models.DateField()),
                ('campaignEndDate', models.DateField()),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('pointEffectiveDate', models.DateField()),
                ('pointExpiryDate', models.DateField()),
                ('IsCampaignCumulative', models.BooleanField(default=False)),
                ('noOfTargetPoints', models.IntegerField(blank=True, null=True)),
                ('noOfTargetCustomers', models.IntegerField(blank=True, null=True)),
                ('pointsGenerated', models.IntegerField(default=0)),
                ('customerReached', models.IntegerField(default=0)),
                ('uniqueCustomerReached', models.IntegerField(default=0)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
