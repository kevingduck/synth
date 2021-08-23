# This script synthesizes the sound of a keyboard. 
import numpy as np
import pyaudio
import time
import wave
import sys

# Global variables
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Function to generate the sound of a keyboard
def generate_sound(key_pressed):
        # Generate the sound of a key
    key_sound = np.zeros(CHUNK)
    for i in range(len(key_sound)):
        key_sound[i] = np.sin(2 * np.pi * 440 * i / RATE) * np.sin(2 * np.pi * key_pressed * i / RATE)

        # Generate the sound of a white noise
    
    white_noise = np.random.rand(CHUNK)
    white_noise = white_noise - 0.5
    white_noise = white_noise * 2

        # Generate the sound of a keyboard
    keyboard_sound = np.zeros(CHUNK)
    for i in range(len(keyboard_sound)):
        keyboard_sound[i] = np.sin(2 * np.pi * 440 * i / RATE) * white_noise[i]

        # Generate the sound of a piano
    piano_sound = np.zeros(CHUNK)
    for i in range(len(piano_sound)):
        piano_sound[i] = np.sin(2 * np.pi * 440 * i / RATE) * np.sin(2 * np.pi * key_pressed * i / RATE) * white_noise[i]


# Function to play the sound
def play_sound(sound):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)
    stream.write(sound.astype(np.int16).tostring())
    stream.stop_stream()
    stream.close()
    p.terminate()
    

# Function to record the sound
def record_sound():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to play the recorded sound
def play_recorded_sound():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
    stream.write(wf.readframes(CHUNK))
    stream.stop_stream()
    stream.close()
    p.terminate()


# main function
def main():
    record_sound()

    # Play the sound
    play_recorded_sound()

    # Generate the sound of a key
    generate_sound(int(sys.argv[1]))

main()