import time
import pygetwindow as gw
from plyer import notification

ICON_PATH = "sad.ico"
WATCHED_APPS = ["discord", "youtube", "steam"]

# Track notifications per app
notified_apps = {app: False for app in WATCHED_APPS}

def get_active_window():
    try:
        window = gw.getActiveWindow()
        return window.title if window else ""
    except Exception as e:
        print(f"[ERROR] Failed to get active window: {e}")
        return ""

while True:
    active_window = get_active_window().lower()

    for app in WATCHED_APPS:
        if app.lower() in active_window:
            if not notified_apps[app]:
                print(f"[DEBUG] {app.capitalize()} detected, sending notification...")
                notification.notify(
                    title="- mrcoolguy",
                    message=f"😢 pls study ? ({app.capitalize()})",
                    timeout=5,
                    app_icon=ICON_PATH
                )
                # Mark that we've sent a notification
                # NOTE: this isnt 100% working, it will send multiple notifications while ur in the app if u click to close the notification (as closing it)
                # and then still being in the app is a window focus event, thus making the code think ur not on the app (ur on the notification)
                # then thinking u switch back to the app...
                notified_apps[app] = True
        else:
            # Reset when the app is unfocused
            notified_apps[app] = False

    # check every 200ms
    time.sleep(0.2)
