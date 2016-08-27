from django.core.management.base import BaseCommand, CommandError
from uploadcsv.models import Namelist, NamelistForm
import datetime

class Command(BaseCommand):
    help = 'Procesa CSV y encuentra coincidencias en Panama Papers'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for namelist in Namelist.objects.all():
            if namelist.status != "Procesado1":
                try:
                    print namelist.namefile

                except:
                    raise CommandError('Error "%s" procesando' % namelist.namefile)

                namelist.donefile = namelist.namefile.name.join("_done");
                namelist.done_date = datetime.datetime.now()
                namelist.status = "Procesado";
                namelist.save()

                self.stdout.write(self.style.SUCCESS('Successfully processed "%s"' % namelist.donefile))
