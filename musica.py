#!/usr/bin/env python
import os, time

firstOctaveLa = 440
noteNames = ['do', 'dos', 're', 'res', 'mi', 'fa', 'fas', 'sol', 'sols', 'la', 'las', 'si']
laPos = 9
noteFreqs = {}

def location (elt, list):
    return [i for i,x in enumerate(list) if x == elt][0]

for i, n in enumerate (noteNames):
    noteFreqs[n] = firstOctaveLa * pow(2, (i - laPos)/12.0)

def freq (note, octave=1):
    return octave * noteFreqs[note]

def beep (note, octave=1, l=1000):
    os.system ('beep -f ' + str(freq(note, octave)) + ' -l ' + str(l))

def pause (l=1000):
    time.sleep(l/1000.0)

def accelerate (song, ratio):
    return map (lambda x:
                    [x[0], x[1]*ratio],
                song)


hendrix = []

smokeOnTheWater = [
    ['mi', 500],
    ['sol', 500],
    ['la', 750],
    ['s',250],
    #
    ['mi', 500],
    ['sol', 500],
    ['las', 250],
    ['la', 750],
    ['s',250],    
    #
    ['mi', 500],
    ['sol', 500],
    ['la', 750],
    ['s', 125],
    #
    ['sol', 625],
    ['mi', 1000],
]

lalo = [
    ['si', 250],
    ['si', 250],
    ['do', 250],
    ['re', 250],
    ['re', 250],
    ['do', 250],
    ['si', 250],
    ['la', 250],
    ['sol', 250],
    ['sol', 250],
    ['la', 250],
    ['si', 250],
    ['si', 250],
    ['la', 250],
    ['la', 500],
    #
    ['si', 250],
    ['si', 250],
    ['do', 250],
    ['re', 250],
    ['re', 250],
    ['do', 250],
    ['si', 250],
    ['la', 250],
    ['sol', 250],
    ['sol', 250],
    ['la', 250],
    ['si', 250],
    ['la', 250],
    ['sol', 250],
    ['sol', 500],
]

for note, length in accelerate (smokeOnTheWater, 0.8):
    if note == 's':
        pause(length)
    else:
        beep (note, l=length)

for note, length in accelerate (lalo, 0.8):
    if note == 's':
        pause(length)
    else:
        beep (note, l=length)
