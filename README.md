# Pwnagotchi showPassLE.py Plugin

Displays the most recent cracked password on the Pwnagotchi display. It currently processes the wpa-sec potfile generated by the Pwnagotchi wpa-sec.py plugin. Support for OnlineHashCrack is a goal. Feel free to help out if you want.

# Installation A

1. SSH into your Pwnagotchi and create a new folder for third-party Pwnagotchi plugins. I use `/root/custom_plugins/` but it doesn't really matter: `mkdir /root/custom_plugins/`
1. Grab the `display-password.py` and `display-password.toml` file from this Github repo and put it into that custom plugins directory.
1. Edit `/etc/pwnagotchi/config.toml` and change the `main.custom_plugins` variable to point to the custom plugins directory you just created: `main.custom_plugins = "/root/custom_plugins/"`
1. In the same `/etc/pwnagotchi/config.toml` file, add the following lines to enable the plugin:
```
main.plugins.showPassLE.enabled = true
main.plugins.showPassLE.pos_x = 0
main.plugins.showPassLE.pos_y = 96
```
Once the above steps are completed, reboot the Pwnagotchi to ensure all changes are applied.

# Installation B

I prefer to install plugins a different way, heres how I do it

1. SSH into your Pwnagotchi and (assuming you have a custom-plugins foler), type `cd /usr/local/share/pwnagotchi/custom-plugins/`
1. type `sudo wget https://raw.githubusercontent.com/usernameLeon27/pwnagotchi-display-password-plugin/refs/heads/master/showPassLE.py`
1. type `config` and add these lines:
```
main.plugins.showPassLE.enabled = true
main.plugins.showPassLE.pos_x = 0
main.plugins.showPassLE.pos_y = 96
```
4. type `pwnkill` to reboot and the plugin should work!

# Common Display Coordinates

THESE COORDINATES MAY OR MAY NOT BE ACCURATE.

These are the coordinates in the original code, I only tested on a waveshare_v4 on [jayofelony's image](https://github.com/jayofelony/pwnagotchi). Results may vary.

| Display Model  | Coordinates (x, y) |
| ------------- | ------------- |
| waveshare_v1, waveshare_v2, waveshare_v3, waveshare_v4  | (0, 96)  |
| waveshare144lcd  | (0, 92)  |
| inky  | (0, 83)  |
| waveshare2in7  | (0, 153)  |
| waveshare1in54V2  | (0, 92)  |
| default  | (0, 91)  |

# Screenshots:

**Network name** - ***Password***

**DESKTOP-0N3H3J4 2624** - ***testtest***

| Cracked | Nothing Cracked |
| ------- | --------------- |
| ![pwnyCrackReal.jpg](images/pwnyCrackReal.jpg?raw=true  "showPassLE.py") | ![pwnyNoCrackReal.jpg](images/pwnyNoCrackReal.jpg?raw=true "showPassLE.py") |
| ![pwnyCrack.png](images/pwnyCrack.png?raw=true "showPassLE.py") | ![pwnyNoCrack.png](images/pwnyNoCrack.png?raw=true "showPassLE.py") |



