from winotify import Notification, audio
import time
import os

# if you run this program it will send you notifications infinitly
# only way to stop this by killing the terminal

STOP_FILE = "stop.flag"


def send_notification():
    toast = Notification(
        app_id="Python app",
        title="Hii Ashish",
        msg="Its time for you to take a break or drink some water",
    )
    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Skip", launch="")
    toast.add_actions(label="Stop reminders", launch=os.path.abspath("stop.bat"))

    toast.show()


while True:
    if os.path.exists(STOP_FILE):
        print("Program stopped forever by user.")
        break
    send_notification()
    time.sleep(5)
