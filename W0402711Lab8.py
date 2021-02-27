from guizero import App, Slider,TextBox
from gpiozero import AngularServo
import time 

#Servo1 is related to 
Servo1 = 17
Servo2 = 18

minpw = (1/1000)
maxpw = (2/1000)

#slider_change1 and slider_change2 are two nearly identical functions used for controlling each of the two necessary servo motors
#slider_change1 is in charge of controlling servo1 and making the slider's value control its placement
def slider_change1(slider1_value):
    text1.value = slider1_value
    servo1 = AngularServo(Servo1, min_pulse_width = minpw, max_pulse_width = maxpw, initial_angle = 0, min_angle = 0, max_angle = 180)
    servo1.angle = int(slider1_value)    
    time.sleep(.25)
    
def slider_change2(slider2_value):
    text2.value = slider2_value
    servo2 = AngularServo(Servo2, min_pulse_width = minpw, max_pulse_width = maxpw, initial_angle = 0, min_angle = 0, max_angle = 180)
    servo2.angle = int(slider2_value)
    time.sleep(.25)

if __name__ == '__main__':
    app = App()
    slider1 = Slider(app, start=0, end=180, width="fill",command = slider_change1)
    text1 = TextBox(app)
    slider2 = Slider(app, start=0, end=180, width='fill', command = slider_change2)
    text2 = TextBox(app)
    app.display()