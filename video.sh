fbset -xres 1920 -yres 1080 -depth 16
setterm -blank 0 -powersave off -powerdown 0
while true ; do
omxplayer -r /home/pi/TV*.wmv
done
