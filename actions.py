import serial
import time
import json
from enum import Enum
from RobopetFaceDetect.main import face_recognize
from pygame import mixer


class Sound(Enum):
    BARK_TWICE = 1
    HAPPY_BARK = 2
    MEDIUM_ANGRY_BARK = 3
    SCARY_BARK = 4


sound_files = {
    Sound.BARK_TWICE: "sounds/bark_twice.wav",
    Sound.HAPPY_BARK: "sounds/happy_barks.wav",
    Sound.MEDIUM_ANGRY_BARK: "sounds/medium_angry_bark.wav",
    Sound.SCARY_BARK: "sounds/scary_bark.wav"
}


def init_serial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    return ser


def send_serial_cmd(cmd):
    ser = init_serial()
    ser.write(bytes(cmd+"#", "UTF-8"))


def make_sounds(sound):
    """
    make the dog bark
    :param sound: enum of type Sound
    :return: void
    """
    mixer.init()
    mixer.music.load(sound_files[sound])
    mixer.music.set_volume(1.0)
    if not mixer.music.get_busy():
        mixer.music.play()