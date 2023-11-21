Lab 8: Seeing is Believing
========================

Give Pupper the ability to see! In this lab, you'll be using Pupper's OAK-D camera to recognize and track a person (in place).

`Lab Document <https://docs.google.com/document/d/1E9m5CkxJx1agDqbwgxrIn9BYTjTdWUYTpshVoe7uvxg/edit?usp=sharing>`_ 

`Lab Review Slides <https://docs.google.com/presentation/d/1sjY9XK81GSq5iTafxziCz354rBoAEb1O/edit?usp=sharing&ouid=112164671976474020631&rtpof=true&sd=true>`_ 

**Goals:**
        1. Use computer vision to detect people.
        2. Program pupper to track people in place using bounding boxes.


Step 1. SSH into the Pupper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ../../../_static/internet_sharing.png
    :align: center
    :width: 50%
#. Before starting the SSH, share network between your host machine and its remotes. In System Preferences, open "Sharing". In this window, you should see "Internet Sharing". Expand the options there, and enable all LAN connections so that we can share network over the ethernet connection to the Raspberry Pi. Turn on Internet Sharing. 
#. With the fully built Pupper, plug an ethernet cable between your laptop and the Pupper's Raspberry Pi, using an ethernet to usb adapter if needed (provided, ask a TA).  

.. figure:: ../../../_static/ethernet.jpg
    :align: center
    :width: 50%

#. Like the RL lab, we can SSH into a remote system inside VSCode. Open VSCode, and use ``CMD + Shift + P`` to access the Command Pallete.
#. In the Command Pallette, type in ``pi@raspberrypi.local`` to prompt a remote connection. This will allow you to ssh into the Pupper's Raspberry Pi via the ethernet connection. 
#. When the Enter Password prompt shows, enter ``raspberry`` as the password. This is a default password on the Raspberry Pis, you may change it if you like (be sure to remember it!). VSCode will tell you if your SSH connection was successful. You can use the Command Pallete to navigate around the Raspberry Pi and use the Terminal to run commands. 

Step 2. Clone the starter code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. For this lab, the code will run directly on your Pupper, which is why we have to SSH into the Raspberry Pi. Once SSH'd create a new directory for CS123 under home, and ``cd`` into it, and clone the lab 7 starter code. Install the package prequisites.

``mkdir ~/CS123``

``cd CS123``

``git clone https://github.com/cs123-stanford/lab_8_seeing_is_believing.git``

#GABRAEL PLEASE EDIT THIS SECTION

Step 3. Edit vision.py to determine where the Pupper should be looking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 4. Edit control.py to update Pupper's velocity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 5. Run your code on Pupper!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

