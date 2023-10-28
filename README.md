**NOTICE: If you have any Errors or Bugs -> Open an Issue or Contact me via Discord: voidyyz or E-Mail: admin@centrapi.net

# NanoKontrolProfiler
A Program to use multiple Profiles on one Nanokontrol (just like if you had two or more - up to 15)

## Requirements:
- Python 3.8 or above
- LoopMidi Installed (https://www.tobias-erichsen.de/software/loopmidi.html) # Not Required on MacOS
- Have Microsoft Buildtools Installed (https://aka.ms/vs/17/release/vs_BuildTools.exe) # Not Required on MacOS

## Installation:
1. In LoopMidi create a new Virtual Device called **pymid** # Not Required on MacOS
2. Open a new Command Line in the NanoKontrolProfiler
3. Type: `pip install -r requirements.txt`
4. Open the **main.py** File
5. In FL Studio select pymid instead of your Nanokontrol as MIDI Controller

## Guide:

**Remember to start loopmidi every time before opening this script**

After the Program has started, click on Settings.
With the Button "Set Up" you can set, which Button on the 
Nanokontrol is used to increase the Profile Value
For that, Press the "Set Up" Button and then Press the Button
you want to map it to

Same goes for the "Set Down" Button which is used to Decrease 
the Profile Value

With the "Exclude Button" Button,
you can Set Buttons that are always sent on Profile one. 
(Used if you want a Button oder Fader to always do the Same effekt)
Just press the "Exclude Button" Button and then Press the Button on your Nanokontrol

With the "Reset Excludes" Button, you can Remove all Buttons you have added to the Exludes
