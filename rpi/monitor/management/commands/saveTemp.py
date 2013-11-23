from django.core.management.base import NoArgsCommand

from monitor.models import Temperature
import smbus


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        self.stdout.write('starting\n')

        bus = smbus.SMBus(1)
        address = 0x48

        bus.write_byte_data(address, 0xac, 0x00)  # tryb ciaglego pomiaru
        bus.write_byte(address, 0xee)  # rozpoczyna pomiar

        self.stdout.write('done\n')

        u2_temperature = bus.read_word_data(address, 0xaa)  # odbiera dane w kodzie U2
        new_temperature = u2_temperature % 256 
        if (u2_temperature > 0xFF):
            new_temperature += 0.5
        self.stdout.write("u2_temperature: %f 'C" % new_temperature)

        temperature_to_save = Temperature(temperature=new_temperature)
        temperature_to_save.save()
