Lab 6: Seeing is Believing
======================================

*Goal: Use computer vision to give your Pupper a sense of sight. At the end of this lab, Pupper should be able to track a person using its camera.*

Step 1. Install X11 SSH into the Raspberry Pi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 2. Connect the Raspberry Pi to Stanford Wifi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 3. Install DepthAI on the Raspberry Pi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use any of the Tiny YOLO models.

Step 4. 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


pseudocode for script 1:
#stand in place pupper

find the center of the person boundary box using xmin + x max/2, ymin + ymax/2
find the distance of that center from (0.5, 0.5) using the distance equation
assign the velocity to be proportional that distance * some constant that has to be tuned
send the velocity to the other script

if no person is found, make the pupper return to center

script 2:
receives the velocity and calls the pupper api update function for yaw control


