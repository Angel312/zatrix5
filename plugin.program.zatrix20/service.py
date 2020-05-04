#-*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urllib2,urllib
import re
import time
xbmc.sleep(10000)
xbmc.executebuiltin('UpdateAddonRepos')
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
CHECKVERSION  =  os.path.join(USERDATA,'versioncheck.txt')
my_addon = xbmcaddon.Addon()
dp = xbmcgui.DialogProgress()
checkver=my_addon.getSetting('checkupdates')
dialog = xbmcgui.Dialog()
if not os.path.exists(CHECKVERSION):
		file = open(CHECKVERSION,'w')
		file.write("<build>ZATRIX</build><version>2020.05.01</version>")
		file.close()
checkurl = "https://pastebin.com/raw/V5QpVNib"
vers = open(CHECKVERSION, "r")
regex = re.compile(r'<build>(.+?)</build><version>(.+?)</version>')
for line in vers:
	if checkver!='false':
		currversion = regex.findall(line)
		for build,vernumber in currversion:
			if vernumber > 0:
				req = urllib2.Request(checkurl)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				match = re.compile('<build>'+build+'</build><version>(.+?)</version>').findall(link)
				for newversion in match:
					if newversion > vernumber:
						yes_pressed = xbmcgui.Dialog().yesno("[B]Build Update[/B]", 'Er staat een update voor u klaar', 'Wilt u uw de Build nu bijwerken?', '', yeslabel='JA',nolabel='LATER')
						if yes_pressed:
							dialog.ok('[B]Build Update[/B]','Klik op [B]OK[/B] om de update uit te voeren.')
							xbmc.executebuiltin("ActivateWindow(10001,plugin://plugin.program.zatrix20/?url=&mode=2,return)")
						else:
							dialog.ok('[B]Build Update[/B]','U kunt de Build bijwerken de volgende keer dat u herstart/opstart.','','')
