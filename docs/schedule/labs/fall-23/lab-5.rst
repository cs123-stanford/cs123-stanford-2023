Lab 5 - Pupper Assembly (WIP)
========================

.. contents:: :depth: 2

Step 1.Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Detach your robot arms from the base 
#. Attach 2 motors, one into each side of motor bulkhead, with 3 M3x6 phillips head screws each
#. Attach left and right legs to the shafts of the motors you just installed and screw in shoulder bolt tightly
#. Thread the wrapped cables through slots
#. Zip tie the cables to keep them in place
#. Clip motor controllers into place
#. Connect motor and encoder cables to motor controllers
#. Repeat this process so you have two motor bulkheads with four legs total

DELIVERABLE: Screen recording of stand up in simulation

Step 2. Deploy Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/Xhj-rCPxm6o" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

#. Detach your robot arms from the base 
#. Attach 2 motors, one into each side of motor bulkhead, with 3 M3x6 phillips head screws each
#. Attach left and right legs to the shafts of the motors you just installed and screw in shoulder bolt tightly
#. Thread the wrapped cables through slots
#. Zip tie the cables to keep them in place
#. Clip motor controllers into place
#. Connect motor and encoder cables to motor controllers
#. Repeat this process so you have two motor bulkheads with four legs total

DELIVERABLE: Take video of stand-up

CHECK. Ensure Motor IDs are correct
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use this diagram to ensure you have the correct IDs set on your motor controllers. For each bulkhead you should have:

Right left/right motion hip motor: 1

Right forward/back motion hip motor: 2

Right knee motor: 3

Left left/right motion hip motor: 4

Left forward/back motion hip motor: 5

Left knee motor: 6


.. figure:: ../_static/motor_ids.png
    :align: center
    
    Motor ID diagram

Step 3. Walking Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/vv3jABUq3ng" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

#. Place front motor bulkhead
#. Connect motor controller power cables (yellow XT30) and CAN connectors (small white JST GH) to bottom PCB
#. Place back motor bulkhead and connect cables
#. Flip robot and fasten bulkheads to bottom PCB with 4x M3x6 button head screws
#. Tighten these screws well and/or add loctite 

DELIVERABLE: What terms are included in your reward functions? What coefficeints did you use? How did you come up with these terms and what was their desired effect? Why might this policy perform poorly on the physical robot?

Step 4. Domain Randomization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/OArwzrKzQdM" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

#. Screw RPi into electronics bulkhead with M2.5x5 socket head screws such that the Pi is oriented like in the video.
#. Connect USB C extension cable to Rpi
#. Connect RPi camera flex cable into RPi. There's a little grey flap that flips up on the connector that lets you slide the cable in. Flip the flap down to lock the cable in.
#. Connect RPi to power by using 2-pin cable. Connect one end into 5V, GND pins near the Teensy and other side into RPi. Quadruple-check that the 5V and GND pins are going the right places. See diagram.
#. Connect RPi to Teensy using USB A to USB micro cable
#. Connect RC receiver to RPi with usb extension cable.


DELIVERABLE: What other terms could you randomize?



.. figure:: ../_static/djipupper_photos/startup-position.png
    :align: center
    
    Startup position.


Step 5. Speed/terrain test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/OArwzrKzQdM" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

#. Screw RPi into electronics bulkhead with M2.5x5 socket head screws such that the Pi is oriented like in the video.
#. Connect USB C extension cable to Rpi
#. Connect RPi camera flex cable into RPi. There's a little grey flap that flips up on the connector that lets you slide the cable in. Flip the flap down to lock the cable in.
#. Connect RPi to power by using 2-pin cable. Connect one end into 5V, GND pins near the Teensy and other side into RPi. Quadruple-check that the 5V and GND pins are going the right places. See diagram.
#. Connect RPi to Teensy using USB A to USB micro cable
#. Connect RC receiver to RPi with usb extension cable.


DELIVERABLE: Test your policy during office hours

Resources
-----------

Wiring diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ../_static/wiring-diagram.png
    :align: center
    
    Wiring diagram.
