Lab 7: Do What I Say
========================

Now we are ready to do some cool things! With the fully built Pupper, we are going to use LLMs to control the robot to do new tasks that we can come up with, making new movements faster than we could have imagined!


**Goals:**
        1. Use LLMs to program Pupper to perform new tasks on the fly.
        2. Use prompt engineering for an open-ended mini project!

TODO ADD IMAGE

Step 1. SSH into the Pupper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. With the fully built Pupper, plug an ethernet cable between your laptop and the Pupper's Raspberry Pi, using an ethernet to usb adapter if needed (provided, ask a TA).  TODO INSERT PHOTO OF ADDING ETHERNET CABLE
#. Open a terminal window on your computer. Run the command ``ssh pi@raspberrypi.local``. This will allow you to ssh into the Pupper's Raspberry Pi via the ethernet connection. 
#. When the Enter Password prompt shows, enter ``raspberry`` as the password. This is a default password on the Raspberry Pis, you may change it if you like (be sure to remember it!). Your terminal window should show that you are in the Pi if the SSH was successful. 

Step 2. Clone the starter code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. For this lab, the code will run directly on your Pupper, which is why we have to SSH into the Raspberry Pi. Once SSH'd create a new directory for CS123 under home, and ``cd`` into it, and clone the lab 7 starter code. Install the package prequisites.
``mkdir ~/CS123``
``cd CS123``
``git clone https://github.com/cs123-stanford/lab_7_llms.git``
``pip3 install -r requirements.txt``
After running the ``pip install`` command, you should see that openai has been installed. If not, ask a TA.

Step 3. Add in OpenAI API Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. For working with ChatGPT from a script, you must have an API key. This API key allows you to make a request to the ChatGPT api from your script, and tells OpenAI the associated account that is making the request (each API call has a small charge associated with it). For the lab, we will be using a shared API key. Check your Canvas announcements for the API key, and copy that API key as a string into ``constants.py`` under ``OPEN_AI_API_KEY``.
#. Save the file before the next step.

Step 4. Chat with ChatGPT in the command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. In VSCode, open ``simple_conversation.py``. This file provides the framework for starting a simple conversation with ChatGPT. Open a new terminal (top bar, Terminal -> New Terminal). 
#. Run ``simple_conversation.py`` in the terminal window``
#. Once run, you should see a chat window open with ChatGPT. You should be able to chat with the ChatGPT from your terminal, just like in the web app. Play around and chat with ChatGPT. 

**Deliverable: Take a look at simple_conversation.py, and write a sentence about how it works. How does the ``get_response()`` function work?**


**Deliverable: Write about why we are doing an IK -> FK consistency test rather than an FK -> IK test (2-3 sentences). Hint: Think about the robot leg configuration(s)**

**Deliverable: Why is it important that the point we are testing is reachable? Describe what you expect IK to return for this case?**

Step 4. Put it together! Make your two robot arms match each other's end-effector positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Implement the rest of ``loop()`` in ``main.cpp`` and deploy on the robot

**Deliverable: Send a video of the arms roughly matching each other when you move them**

2. Try more iterations of IK in ``kinematics.h``, and observe the behavior **(Careful may be unstable)**

**Deliverable: Why does more iterations of IK cause instability?**
