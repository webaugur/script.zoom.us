import os
import sys
import subprocess
import xbmcaddon
import xbmcgui
 
# Zoom URL Format
#    zoommtg://zoom.us/join?action=join&confno=<MEETING ID>
zoom_url         = "zoommtg://zoom.us/join\?action=join\&confno="
zoom_exec        = "/usr/bin/zoom"
addon       = xbmcaddon.Addon()

# If Zoom is executable then ask for Meeting ID
if os.access(zoom_exec, os.X_OK):
    # Meeting ID Input Dialog.
    #   Kodi should scrub the input as long as we are set to Numeric...
    zoom_meetid = xbmcgui.Dialog().input("Zoom.US Meeting ID", "", xbmcgui.INPUT_NUMERIC)

    # Execute Zoom without a shell
    subprocess.run([zoom_exec, " ", zoom_url, zoom_meetid])

# If zoom is not executable then ask the user to install Zoom
else: 
    xbmcgui.Dialog().ok("Zoom Error", "Please install Zoom from https://zoom.us to /usr/bin/zoom")

