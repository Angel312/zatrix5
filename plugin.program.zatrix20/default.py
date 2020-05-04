#-*- coding: utf-8 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib2,urllib
import re
import extract
import time
import downloader
import plugintools
import zipfile
import ntpath
import base64

databasePath = xbmc.translatePath('special://database')
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
thumbnailPath = xbmc.translatePath('special://thumbnails');
thumbdir = xbmc.translatePath('special://thumbnails')
tempPath = xbmc.translatePath('special://temp')
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='http://www.none.com'
ADDON=xbmcaddon.Addon(id='plugin.program.zatrix20')
dialog = xbmcgui.Dialog()
VERSION = "1.0.0"
PATH = "afkbox"


def index():
    addDir('Zatrix Update','',2,'http://addons.allefilmskijken.com/images/update.png','http://addons.allefilmskijken.com/images/achtergrond.png','')
    addDir('Zatrix Extra','',3,'http://addons.allefilmskijken.com/images/update.png','http://addons.allefilmskijken.com/images/achtergrond.png','')
    setView('movies', 'MAIN')

def update():
    link = OPEN_URL('https://pastebin.com/raw/m7mceK9s').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description, folder=False)
    setView('movies', 'MAIN')

def extra():
    link = OPEN_URL('http://addons.allefilmskijken.com/update/extra.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,4,iconimage,fanart,description, folder=False)
    setView('movies', 'MAIN')

def updateAUTH():
    AUTHENTICATE()
    link = OPEN_URL('https://pastebin.com/raw/m7mceK9s').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description, folder=False)
    setView('movies', 'MAIN')


def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link


def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib)
    if os.path.exists(lib):
        addonfolder = xbmc.translatePath(os.path.join('special://','home'))
        time.sleep(2)
        dp = xbmcgui.DialogProgress()
        dp.create("Uw systeem wordt nu bijgewerkt.",'', 'Wacht geduldig af tot volgende venster verschijnt.')
        dp.update(0,"", "ZIP wordt uitgepakt - even geduld")
        print '======================================='
        print addonfolder
        print '======================================='
        extract.all(lib,addonfolder,dp)
        dp.close()
        try: os.remove(lib)
        except: pass
        dialog = xbmcgui.Dialog()
        dialog.ok("Build Updater", "De Box moet worden herstart om de installatie met succes af te ronden. Klik op OK deze te sluiten.")
        os._exit(1)

def AUTHENTICATE():
    DATA_SETTINGS_FILE   =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.program.zatrix20/settings.xml'))

    if not os.path.exists(DATA_SETTINGS_FILE):
        xbmcgui.Dialog().ok("[B][COLOR cyan]Zatrix Build[/COLOR][/B]", "Actieve subscription is nodig voor [B][COLOR cyan]Zatrix build[/COLOR][/B]!", "Vul AUB uw email adres in bij het volgende scherm!", "Nog geen subscription? - [COLOR cyan]www.gettv.nl/subs[/COLOR]")
        xbmcaddon.Addon().openSettings()

    if not os.path.exists(DATA_SETTINGS_FILE):
        sys.exit(1)

    email = xbmcaddon.Addon().getSetting("Email")

    email=email.replace(' ','')


    url = base64.b64decode('aHR0cDovL2dldHR2Lm5sLw==') + email

    f = urllib.urlopen(url)
    data = f.read()
    f.close()

    if not base64.b64decode('QWxsb3c=') in data:
		dialog       =  xbmcgui.Dialog()
		dialog.ok('[B][COLOR cyan]Zatrix Build[/COLOR][/B]', "[B][COLOR red]Error:[/COLOR][/B] Geen geldige email of actieve subscription.", "Controleer deze of neem contact op met [COLOR cyan]info@gettv.nl[/COLOR] ")
		xbmcaddon.Addon().openSettings()
		sys.exit(0)

def wizardrem(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib)
    if os.path.exists(lib):
        addonfolder = xbmc.translatePath(os.path.join('/storage/'))
        time.sleep(2)
        dp = xbmcgui.DialogProgress()
        dp.create("Uw systeem wordt nu bijgewerkt.",'', 'Wacht geduldig af tot volgende venster verschijnt.')
        dp.update(0,"", "ZIP wordt uitgepakt - even geduld")
        print '======================================='
        print addonfolder
        print '======================================='
        extract.all(lib,addonfolder,dp)
        dp.close()
        try: os.remove(lib)
        except: pass
        dialog = xbmcgui.Dialog()
        dialog.ok("Build updater", "De Box moet worden herstart om de installatie met succes af te ronden. Klik op OK deze te herstarten.")
        xbmc.executebuiltin('Reboot')

def removefolder(map):
    if os.path.exists(map)==True:
        for root, dirs, files in os.walk(map, topdown=False):
            for name in files:
                try: os.remove(os.path.join(root, name))
                except: pass
            for name in dirs:
                try: os.rmdir(os.path.join(root, name))
                except: pass

def addDir(name,url,mode,iconimage,fanart,description,folder=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=folder)
        return ok



def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass


print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )


if mode==None:
    index()

elif mode==1:
    wizard(name,url,description)

elif mode==2:
    update()

elif mode==3:
	extra()

elif mode==4:
    wizardrem(name,url,description)

xbmcplugin.endOfDirectory(int(sys.argv[1]))