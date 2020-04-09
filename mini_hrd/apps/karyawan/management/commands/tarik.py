from django.core.management.base import BaseCommand
from karyawan.views import inserting_data_tes, look_data_tes

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='?')

        parser.add_argument('-a', '--all', action='store_true', help='Create an admin account')

    def handle(self, *args, **options):
        all = options['all']

        if all:
            look_data_tes()
        else :
            inserting_data_tes()
        
        print "ok %s" % options['sample']
