from soco import SoCo
from time import sleep
from random import randrange

livingroomSonos = SoCo('192.168.1.16')
gameroomSonos = SoCo('192.168.1.35')
masterbedroomSonos = SoCo('192.168.1.15')
patioSonos = SoCo('192.168.1.14')

devices = [livingroomSonos, gameroomSonos, masterbedroomSonos, patioSonos]

def playSound():
    livingroomSonos.volume = 0
    gameroomSonos.volume = 0
    masterbedroomSonos.volume = 0
    patioSonos.volume = 0

    boom = 'https://www.myinstants.com/media/sounds/vine-boom.mp3'
    someonesHere = 'https://www.myinstants.com/media/sounds/someones-here.mp3'
    atDoor = 'https://www.myinstants.com/media/sounds/atthedoor.mp3'
    evermore1 = r'https://www.mboxdrive.com/yt1s.com%20-%20Taylor%20Swift%20%20evermore%20Official%20Lyric%20Video%20ft%20Bon%20Iver.mp3'
    seeMeUpstairs = r'https://www.mboxdrive.com/ttsMP3.com_VoiceText_2021-10-19_22_42_31.mp3'
    sweetDreams = r'https://www.mboxdrive.com/bedbugs1.mp3'
    hourboom = r'https://www.mboxdrive.com/yt1s.com%20-%201%20hour%20of%20silence%20occasionally%20broken%20up%20by%20Vine%20boom%20sound%20effect.mp3'
    
    sound = hourboom

    
    for device in devices:
        device.play_uri(sound)

    print(f'Sound Played Across {len(devices)} Sonos Devices!')