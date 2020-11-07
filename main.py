import time

from plyer import notification

if __name__ == '__main__':
 while True:
    notification.notify(
        title = "Please Drink Water Now!",
        message = "Water helps dissolve minerals and nutrients, making them more accessible to the body."
                  "It also helps remove waste products",
        app_icon = "C:\\Users\\hp\Desktop\\pythonProject1\\icon.ico",
        timeout=10  
    )

    time.sleep(60*180)