# PluginUIonPeerPressure
uhh... so... plugin ui on peerpressure (now comes with Proto too). If that doesn't explain it good enough idk what will

## NOTES:
1. This appears not to work with Aurora Dashboard. Most likely they both attempt to hook to the same thing, causing a crash. However I am not sure and have no intentions of looking further into that since I don't use aurora.
2. You need to open any app before this loads. This is most likely an issue of PeerPressure and there's nothing I can do to fix it.
3. Proto Stealth Server is now bundled in. If you want to get XBL connection you will need to allow XBL access from family settings (Passcode is 0000/YYYY). Otherwise you can still use it online for the old dashboards without XBL access, therefore putting the risk of a KV ban close to 0.

## How to change your dashboard:
Proto can emulate 4 dashboard themes: Blades, BetaNXE, NXE and Kinect. PluginUI can emulate 5 guide themes: MiniBladesCarbon (aka the Blades guide), BetaNXE, NXE, Kinect and Metro. By default, this repo sets Proto and PluginUI to emulate NXE.
To change these themes:
1. Open Proto.ini in a text editor on your computer.
2. Find this string: `customDashPath = Usb:\Proto Themes\NXE\dash.xex`.
3. Change NXE to any of the themes listed above. For example, the Blades theme would become `customDashPath = Usb:\Proto Themes\Blades\dash.xex`.
    * If you want to disable Proto's theme entirely, set `customDash` to `false`.
5. Save that and open PluginUI.ini. The process is the same here, replace `Default Theme = NXE` with what you want.
---
# PLEASE NOTE THAT FOR THE DASHBOARDS AND PLUGINUI TO WORK YOU NEED TO SELECT XBOX HOME FROM THE GUIDE, AS SETTING A DEFAULT DASHBOARD WILL THROW AN E71
