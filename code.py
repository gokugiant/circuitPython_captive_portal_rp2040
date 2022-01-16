import ublox_setup
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Arduino Nano RP2040 Connect webserver test")

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")
print("Firmware vers.", esp.firmware_version)
print("MAC addr:", [hex(i) for i in esp.MAC_address])

print("Creationg AP...")
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets)

try:
    wifi.create_ap()
except RuntimeError as e:
    print("could not create AP", e)

print("My IP address is", esp.pretty_ip(esp.ip_address))

