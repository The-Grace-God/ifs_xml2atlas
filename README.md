# **YOU WILL NEED TO PROVIDE THE UNPACKED IFS FILE AND OTHER ASSETS YOURSELF**
<ins>**I WILL NOT BE RESPONSIBLE FOR WHATS DONE WITH THOSE FILES**</ins>

# Requirements
- Pillow
- No need to install something for xml files as its now built into pythin

## This is a tool to try and help with editing ifs files by showing you its texture atlas
When running the script you will need to provide where the "texturelist.xml" is

## CLI Build
This one will only output both in console and in a file the canvas size and where each image goes on the atlas **THIS WILL NOT MAKE A IMAGE BY ITSELF**

## Regular Build
**WIP**\
This is also run in the terminal (despite not saying "CLI" in the name) but instead of outputing where the textures go on the atlas it will try to generate the atlas itself

## Examples
### File
`<?xml version='1.0' encoding='UTF-8'?>`\
`<texturelist compress="avslz">`\
`  <texture cfg="eeb-" format="argb8888rev" mag_filter="linear" min_filter="linear" name="tex000" wrap_s="clamp" wrap_t="clamp">`\
`    <size __type="2u16">4096 4096</size>`\
`    <image name="Image 1">`\
`      <uvrect __type="4u16">2 204 2 204</uvrect>`\
`      <imgrect __type="4u16">0 200 0 200</imgrect>`\
`    </image>`\
`    <image name="Image 2">`\
`      <uvrect __type="4u16">2 370 36 274</uvrect>`\
`      <imgrect __type="4u16">0 368 24 272</imgrect>`\
`    </image>`\
`    <image name="Image 3">`\
`      <uvrect __type="4u16">2 406 2 406</uvrect>`\
`      <imgrect __type="4u16">0 404 0 404</imgrect>`\
`    </image>`\
`  </texture>`\
`</texturelist>`\
\
[XML File](https://github.com/The-Grace-God/ifs_xml2atlas/blob/main/example_ifs/tex/texturelist.xml)

### CLI version
![image](https://github.com/The-Grace-God/ifs_xml2atlas/blob/main/Example/image_2025-07-01_181639963.png?raw=true)\
[Output File](https://github.com/The-Grace-God/ifs_xml2atlas/blob/main/Example/example_Atlas_Data.txt)

### Regular version
![image](https://github.com/The-Grace-God/ifs_xml2atlas/blob/main/Example/image_2025-07-01_192821219.png?raw=true)\
Image output\
![image](https://raw.githubusercontent.com/The-Grace-God/ifs_xml2atlas/refs/heads/main/Example/output.png)\
