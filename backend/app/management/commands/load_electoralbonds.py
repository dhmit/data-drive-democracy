"""
Django management command load_dataset

Updates local db with values from base csv dataset
"""
import os
import pandas

from django.conf import settings
from django.core.management.base import BaseCommand
from app.models import ElectoralBondCDenomination


class Command(BaseCommand):
    """
    Custom django-admin command used to run an analysis from the app/analysis folder
    """
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            'dataset_name',
            type=str,
            action='store',
            help='Name of dataset in app/data folder (with extension)',
        )

    def handle(self, *args, **options):
        # pylint: disable=too-many-locals
        file_name = options.get('dataset_name')
        file_path = os.path.join(settings.DATASET_DIR, 'electoralbonds',file_name)
        df = pandas.read_csv(file_path)

        # TODO: Generalize this to update correct model(s) and columns based on dataset
        for party_name, denomination in zip(df["Name of the Political Party"], df["Denomination"]):
            election = ElectoralBondCDenomination(
                party_name=party_name,
                denomination=denomination
            )
            election.save()
