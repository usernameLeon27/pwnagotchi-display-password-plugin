# showPassLE shows recently cracked passwords on the pwnagotchi display 
#
#
###############################################################
#
# Inspired by, and code shamelessly yoinked from
# the pwnagotchi memtemp.py plugin by https://github.com/xenDE
# forked from https://github.com/c-nagy/pwnagotchi-display-password-plugin
#
###############################################################
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import os


class DisplayPassword(plugins.Plugin):
    __author__ = '@usernameLeon27'
    __version__ = '1.0.1'
    __license__ = 'GPL3'
    __description__ = 'A plugin to display most recent cracked passwords'

    def on_loaded(self):
        logging.info("showPassLE loaded")

    def on_ui_setup(self, ui):
        # Set default options from showPassLE.toml (waveshare_v4)
        pos = (self.options['pos_x'], self.options['pos_y'])
        ui.add_element('showPassLE', LabeledValue(color=BLACK, label='', value='',
                                                   position=pos,
                                                   label_font=fonts.Bold, text_font=fonts.Small))

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('showPassLE')

    def on_ui_update(self, ui):
        path = '/root/handshakes/wpa-sec.cracked.potfile'
        try:
            # Reads the last line of the potfile
            last_line = os.popen(f'tail -n 1 {path} | awk -F: \'{{print $3 " - " $4}}\'').read().rstrip()
            
            # Checks if the last line is empty
            if not last_line.strip():
                # If  last line is empty
                last_line = 'Still listening... nothing cracked yet!'
        except Exception as e:
            # For exception errors such as file not found, permission issues
            last_line = f'Error: {str(e)}'
        
        ui.set('showPassLE', last_line)