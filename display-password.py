# display-password shows recently cracked passwords on the pwnagotchi display 
#
#
###############################################################
#
# Inspired by, and code shamelessly yoinked from
# the pwnagotchi memtemp.py plugin by https://github.com/xenDE
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
    __author__ = '@nagy_craig'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin to display recently cracked passwords'

    def on_loaded(self):
        logging.info("display-password loaded")

    def on_ui_setup(self, ui):
        # Display model: ((h_pos), (v_pos))
        display_positions = {
            'waveshare_v2': ((0, 95), (180, 61)),
            'waveshare_v1': ((0, 95), (170, 61)),
            'waveshare144lcd': ((0, 92), (78, 67)),
            'inky': ((0, 83), (165, 54)),
            'waveshare27inch': ((0, 153), (216, 122)),
            'default': ((0, 91), (180, 61)),
            'waveshare_v4' : ((0,95), (180,61))
        }

        def get_positions():
            if ui.is_waveshare_v2(): return display_positions['waveshare_v2']
            if ui.is_waveshare_v1(): return display_positions['waveshare_v1']
            if ui.is_waveshare144lcd(): return display_positions['waveshare144lcd']
            if ui.is_inky(): return display_positions['inky']
            if ui.is_waveshare27inch(): return display_positions['waveshare27inch']
            return display_positions['default']
        
        h_pos, v_pos = get_positions()

        if self.options['orientation'] == "vertical":
            ui.add_element('display-password', LabeledValue(color=BLACK, label='', value='',
                                                   position=v_pos,
                                                   label_font=fonts.Bold, text_font=fonts.Small))
        else:
            # default to horizontal
            ui.add_element('display-password', LabeledValue(color=BLACK, label='', value='',
                                                   position=h_pos,
                                                   label_font=fonts.Bold, text_font=fonts.Small))

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('display-password')

    def on_ui_update(self, ui):
        last_line = 'tail -n 1 /root/handshakes/wpa-sec.cracked.potfile | awk -F: \'{print $3 " - " $4}\''
        ui.set('display-password',
                    "%s" % (os.popen(last_line).read().rstrip()))
