# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    stockid = models.PositiveIntegerField(db_column='StockID', primary_key=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    employees = models.PositiveIntegerField(db_column='Employees', blank=True, null=True)  # Field name made lowercase.
    capital = models.BigIntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    industryname = models.CharField(db_column='IndustryName', max_length=16)  # Field name made lowercase.
    listeddate = models.CharField(db_column='ListedDate', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'
