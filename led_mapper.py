import cv2
import keyboard
import time

cv2.namedWindow("LED Mapper Capture")
vc = cv2.VideoCapture(1, cv2.CAP_DSHOW)

locations = {}
led_index = 0
num_leds = 50
start = False

while cv2.getWindowProperty('LED Mapper Capture', 0) >= 0:
    rval, frame = vc.read()
    cv2.putText(frame, "Press the Space Bar to Start Capture", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(frame, maxLoc, 5, (255, 0, 0), 2)
    cv2.putText(frame, str(maxLoc), (maxLoc[0]+10, maxLoc[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.line(frame, (0, maxLoc[1]), maxLoc, (255, 0, 0), 1)
    cv2.line(frame, (maxLoc[0], 0), maxLoc, (255, 0, 0), 1)

    cv2.imshow("LED Mapper Capture", frame)
    key = cv2.waitKey(20)

    if start and led_index <= num_leds-1:
        locations[led_index] = maxLoc
        print("LED " + str(led_index) + " location saved as: " + str(maxLoc))
        led_index += 1
        keyboard.write('n\n')
        time.sleep(2)
    if key == 27: #ESC
        break
    elif key == 32: #SPACE
        time.sleep(10)
        start = True

with open('led_locs.txt', 'a') as file:
    for led in locations:
        file.write(str(locations[led]) + '\n')
print("LED locations written to file.")

cv2.destroyWindow("LED Mapper Capture")