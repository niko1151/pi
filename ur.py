from sense_hat import SenseHat
from os import system
import datetime, time

sense = SenseHat()

# Farve skema
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
AM_color = (255, 0, 0)
PM_color = (255, 250, 0)
off = (0, 0, 0)

#horizontal = vandret
#vertical = lodret
vand = False
lod = False
timer12 = False


#Display formattet
def display_binary(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            sense.set_pixel(x, row, color)
        else:
            sense.set_pixel(x, row, off)

#denne besked vises når programmet starter
sense.show_message("Programmet starter")

#while true til at holde uret igang og til at kunne indlæse inputs
while True:
    Time = datetime.datetime.now()

    #Læser input fra controleren
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                #rotere skærmen til 0 grader (lodret)
                sense.clear()
                lod = True
                vand = False
                sense.set_rotation(0)

            if event.direction == "down":
                #slutter programmet og viser en besked
                sense.clear()
                sense.show_message("Programmet slutter")
                system.exit()

            if event.direction == "left":
                #rotere skærmen 90 grader (vandret)
                sense.clear()
                lod = False
                vand = True
                sense.set_rotation(90)

            if event.direction == "middle":
                sense.clear()
                if timer12:
                    timer12 = False
                else:
                    timer12 = True
    if vand:
        if timer12:
            if Time.hour > 12:
                Time.hour -= 12
                sense.set_pixel(0,0, AM_color)
            sense.set_pixel(0,1,PM_color)
            display_binary(Time.hour, 2, hour_color)
            display_binary(Time.minute, 4, minute_color)
            display_binary(Time.second, 6, second_color)
        else:
            display_binary(Time.hour, 2, hour_color)
            display_binary(Time.minute, 4, minute_color)
            display_binary(Time.second, 6, second_color)

    if lod:
        if timer12:
            if Time.hour > 12:
                Time.hour -= 12
                sense.set_pixel(0,0, AM_color)
            sense.set_pixel(0,1,PM_color)
            display_binary(Time.hour, 2, hour_color)
            display_binary(Time.minute, 4, minute_color)
            display_binary(Time.second, 6, second_color)
        else:
            display_binary(Time.hour, 2, hour_color)
            display_binary(Time.minute, 4, minute_color)
            display_binary(Time.second, 6, second_color)
