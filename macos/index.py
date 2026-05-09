import sounddevice as sd
import numpy as np
import time
import webbrowser
import os
import subprocess
ST=5.0  
DELAY_M=0.15
DELAY_F=0.8
COOLDOWN=0.2

last_clap_time = 0
clap_count = 0
BROWSERS = [
    "/Applications/Brave Browser.app",
    "/Applications/Google Chrome.app",
    "/Applications/Firefox.app",
    "/Applications/Safari.app"
]

def open_browser(url):
    for browser in BROWSERS:
        if os.path.exists(browser):
            subprocess.run([
                "open",
                "-a",
                browser,
                url
            ])
            return

def audio_callback(indata, frames, time_info, status):
    global last_clap_time, clap_count

    if status:
        return 

    if indata.size == 0:
        return

    audio_data = indata[:, 0]
    
    if len(audio_data) < 2:
        return

    try:
        diff_data = np.diff(audio_data)
        if diff_data.size > 0:
            sharpness = np.max(np.abs(diff_data)) * 1000
        else:
            return
    except ValueError:
        return
    current_time = time.time()
    if sharpness > ST:
        if current_time - last_clap_time > COOLDOWN:
            time_since_last_clap = current_time - last_clap_time
            if DELAY_M <= time_since_last_clap <= DELAY_F:
                clap_count += 1
            else:
                clap_count = 1
            last_clap_time = current_time
            if clap_count == 2:
                os.system("osascript -e 'set volume output volume 100'")
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                time.sleep(1)
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                time.sleep(3)
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                time.sleep(5)
                open_browser("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                clap_count = 0

if __name__ == "__main__":
    try:
        with sd.InputStream(channels=1, samplerate=44100, blocksize=1024, callback=audio_callback):
            while True:
                time.sleep(0.1)
    except KeyboardInterrupt as err:
        print(err)
