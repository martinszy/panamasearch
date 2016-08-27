from django.core.management.base import BaseCommand, CommandError
from uploadcsv.models import Namelist, NamelistForm
import datetime
import os

from core import match_file


class Command(BaseCommand):
    help = 'Procesa CSV y encuentra coincidencias en Panama Papers'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for namelist in Namelist.objects.all():
            if namelist.status == "Pending" or True:
                namelist.donefile = namelist.namefile.name[namelist.namefile.name.rfind("/"):namelist.namefile.name.rfind(".")] + "_done.csv"
                namelist.status = "Processing"
                namelist.save()

<<<<<<< HEAD
                try:
                match_file(
                    namelist.namefile.name,
                    namelist.namefile.name[:namelist.namefile.name.rfind("/")]+"/"+namelist.donefile
                )
                except:
                    raise CommandError('Error processing "%s"' % namelist.namefile)
=======
                #try:
                match_file(
                        namelist.namefile.name,
                        namelist.donefile
                    )
                #except:
                #    raise CommandError('Error processing "%s"' % namelist.namefile)
>>>>>>> 20a988daa72abe363d7d34e799eecffae3492b78

                namelist.done_date = datetime.datetime.now()
                namelist.status = "Done"
                namelist.save()

                self.stdout.write(self.style.SUCCESS('Successfully processed "%s"' % namelist.donefile))
