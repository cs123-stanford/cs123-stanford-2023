Lab 7: Do What I Say
========================

Now we are ready to do some cool things! With the fully built Pupper, we are going to use LLMs to control the robot to do new tasks that we can come up with, making new movements faster than we could have imagined!


**Goals:**
        1. Use LLMs to program Pupper to perform new tasks on the fly.
        2. Experiment on how LLMs perform with high level and low level control on Pupper. 
        2. Use prompt engineering for an open-ended mini project!

TODO ADD IMAGE

Step 1. SSH into the Pupper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. With the fully built Pupper, plug an ethernet cable between your laptop and the Pupper's Raspberry Pi, using an ethernet to usb adapter if needed (provided, ask a TA).  TODO INSERT PHOTO OF ADDING ETHERNET CABLE
#. Like the RL lab, we can SSH into a remote system inside VSCode. Open VSCode, and use ``CMD + Shift + P`` to access the Command Pallete.
#. In the Command Pallette, type in ``pi@raspberrypi.local`` to prompt a remote connection. This will allow you to ssh into the Pupper's Raspberry Pi via the ethernet connection. 
#. When the Enter Password prompt shows, enter ``raspberry`` as the password. This is a default password on the Raspberry Pis, you may change it if you like (be sure to remember it!). VSCode will tell you if your SSH connection was successful. You can use the Command Pallete to navigate around the Raspberry Pi and use the Terminal to run commands. 

Step 2. Clone the starter code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. For this lab, the code will run directly on your Pupper, which is why we have to SSH into the Raspberry Pi. Once SSH'd create a new directory for CS123 under home, and ``cd`` into it, and clone the lab 7 starter code. Install the package prequisites.

``mkdir ~/CS123``

``cd CS123``

``git clone https://github.com/cs123-stanford/lab_7_llms.git``

``pip3 install -r requirements.txt``

This pip3 install may take some time. After running the ``pip install`` command, you should see that openai has been installed. If not, ask a TA.

Step 3. Make Pupper move in a square
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. The code in this repository depends on the KarelPupper API
#. Take a look at the ``karelPupper.py`` Python file. This file details many functions that abstracts away basic functional elements for Pupper, such as ``wakeup()``, ``moveForward()``, and ``turn()`` which were all created using MPC. Using the commands detailed in ``karelPupper.py``, write code to make Pupper move in a square in ``outputs/script_square.py``.
#. Run this script on Pupper, and see how Pupper performs. 
(TODO: we can have them implement one of the karelpupper commands for MPC exposure/experience??)

**Deliverable: Submit your code for ``script_square.py``. Take a video of Pupper successfully walking in a square.**

**Deliverable: Did Pupper walk in a square successfully on the first try? What tuning did you make for Pupper to walk in the square (delays, speed, angle, etc.)**

Step 4. Add in OpenAI API Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now that we can make Pupper do more complex tasks with simpler, abstracted commands, instead of tuning motor torques, we can use LLMs to do a lot of the work for us!

#. For working with ChatGPT from a script, you must have an API key. This API key allows you to make a request to the ChatGPT api from your script, and tells OpenAI the associated account that is making the request (each API call has a small charge associated with it). For the lab, we will be using a shared API key. Check your Canvas announcements for the API key, and copy that API key as a string into ``constants.py`` under ``OPEN_AI_API_KEY``.
#. Save the file before the next step.

Step 5. Chat with ChatGPT in the command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. In VSCode, open ``simple_conversation.py``. This file provides the framework for starting a simple conversation with ChatGPT. Open a new terminal (top bar, Terminal -> New Terminal). 
#. Run ``simple_conversation.py`` in the terminal window``
#. Once run, you should see a chat window open with ChatGPT. You should be able to chat with the ChatGPT from your terminal, just like in the web app. Play around and chat with ChatGPT. 

.. figure:: ../../../_static/openai.png
    :align: center
    :width: 50%

**Deliverable: Take a look at simple_conversation.py, and write a sentence about how it works. How does the ``get_response()`` function work?**

Step 6. Make a prompted conversation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Open ``prompted_conversation.py``. This file provides creates a prompted conversation with ChatGPT. Run this file, and see how ChatGPT gets prompted before running the script. 

**Deliverable: Change the prompt in ``prompted_conversation.py`` to your liking, and submit your prompt in addition to ChatGPT's default response to your prompt**

Next, we are going to experiment with how ChatGPT controls Pupper using both low level, and high level functions. The high level functions will abstract a lot of the nuance associated with tuning motor torques and speeds away. 


Step 7. ChatGPT for lower level control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. In this step, we are going to see how the LLM performs when controlling Pupper at a lower, less abstracted level. We are going to see how well LLMs can be used to help us with implementing a turn function for Pupper
#. In ``prompted_conversation.py``, change ``A_FANTASTIC_ROLE`` and ``PROMPT`` so that ChatGPT understands the context of the behaviors you want. **NOTE:** The initial response from ChatGPT may take some time, so add "Start by asking how you can help me" at the end of your prompt so that ChatGPT doesn't hang. 
#. Ask ChatGPT to program a ``turn()`` function that calls the turn_for_time() function in karelPupper.py. The parameters we will work with are an angle, speed, and behavior. The behavior can take on three states, shown in ``line 27`` of ``karelPupper.py``. Give this information to ChatGPT, and explain the logic of this pseudocode in your prompt: 

.. code-block:: python

    def turn(self, angle, speed, behavior_state):
        clip speed between positive and negative yaw rates (self.config.max_yaw_rate, -self.config.max_yaw_rate) using np.clip (remember to retain the correct signs!)
        calculate the target time using the formula time = angle / yaw_rate
        call the turn_for_time function as self.turn_for_time(target time, speed, behavior_state)

**NOTE:** You will notice that ChatGPT will not understand the full syntax of your code parameters, hence you can prompt ChatGPT to make the syntax changes. For example, telling ChatGPT that the maximum and minimimum possible yaw rates are given by the positive and negative of the syntax ``self.config.max_yaw_rate`` should help ChatGPT to understand how to clip the yaw rate. 

Step 8. Implement script_square.py to test your turn() function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. There is a placeholder for the turn() function in karelPupper.py. Paste the AI-generated code into the the turn() function. 
#. Using karelPupper() commands detailed in karelPupper.py, make pupper walk in a square using the high-level karel_pupper commands in ``script_square.py``
#. Deploy this to the robot, and test how well Pupper walks in a square.

**NOTE:** you may still need to make syntax changes so that your code will run. Refer to the rest of karelPupper.py to see how to do this. 

Step 9. Use ChatGPT to make pupper walk in a square
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Open ``make_robot_script.py``. This file uses ChatGPT to make karelPupper scripts for you. Run this file, and see how ChatGPT can make scripts for you. Every time you make a script, a new script will be made inside the ``outputs`` directory.
#. Ask ChatGPT here to make pupper walk in a square. 

**Deliverable: Using ``make_robot_script.py``, use ChatGPT to write a script that makes Pupper move in a square. Compare this AI-made script to your previous ``square_script.py``. Take a video of Pupper walking in a square using your AI-made script**

**Deliverable: What are the differences you noticed, can you tune your prompt to make ChatGPT more exactly match your script?**

Step 8. ChatGPT for high level control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Using ChatGPT, make Pupper do a complex task of your choice using the high level control from karelPupper.

**Deliverable: Submit a video of Pupper doing your complex task. Submit the code script as well.**



EXPRESSIVE GAITS
