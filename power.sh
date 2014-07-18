# turns off HDMI display - saves 20ma

/opt/vc/bin/tvservice -off

# turns off all USB & ethernet:
# - saves 100ma on bare model B 
# - saves another 90ma for wifi dongle (so still useful on model A)

if [ "$1" == "off" ]
then 
echo "powering off USB"
sudo sh -c "echo 0x0 > /sys/devices/platform/bcm2708_usb/buspower"
else
echo "powering on USB"
sudo sh -c "echo 0x1 > /sys/devices/platform/bcm2708_usb/buspower"
fi
