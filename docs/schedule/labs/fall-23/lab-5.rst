Lab 5: How to Train Your Dog
========================

*Goal: Use RL to control your Pupper.*

Step 1. Set Up Virtual Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Video of GCP Setup

#. Log into GCP and find the gcp-robotics project
#. Start your machine, and SSH into the instance
#. Navigate to the directory "jvclark/rl/legged_gym". Here, you will be able to run the train.py script to train a policy, and play.py script to run the latest policy.

Step 2. VS Code SSH Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Video of VS Code Setup

#. Install the VS Code SSH extension.
#. Press Cmd + Shift + P. Then, configure SSH hosts. Fill out GCP host config as shown in the video.
#. Press Cmd + Shift + P again. Then select "Connect to Host". Press Cmd + O and select the rl/legged_gym repository.
#. You should now be able to edit your code in the legged_gym repo.

Step 3. Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the base height reward function so that Puppper stands up.

#. Edit the  ''_reward_base_height'' ``cd lab_1_hello_pd``
#. Deploy on real

DELIVERABLE: Screen recording of stand up in simulation

Step 4. Deploy Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Transfer policy from local machine to pupper
#. The model is a .pt file under the log folder name (e.g., “model_700.pt”)
#. ‘scp [model name] pi@raspberrypi.local:’ (note the colon at the end)

#. In local puppersim repo, change the policy called in isaac_gym_policy.py (located under the puppersim folder) to your policy name (your .pt file)
#. Change pi address in deploy_to_robot.sh
#. ./deploy_to_robot.sh python puppersim/puppersim/isaac_gym_policy.py --run_on_robot


DELIVERABLE: Video of stand-up in real

DELIVERABLE: Video of stand-up in real


.. figure:: ../_static/motor_ids.png
    :align: center
    

Step 5. Walking Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. We provide basic interface (how to read robot velocity, how to obtain target velocity) and student need to write a new reward function
#. deploy in sim

DELIVERABLE: What terms are included in your reward functions? What coefficeints did you use? How did you come up with these terms and what was their desired effect? Why might this policy perform poorly on the physical robot?

Step 6. Domain Randomization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. Student need to implement domain randomization
#. Deploy on real, works



DELIVERABLE: What other terms could you randomize?



.. figure:: ../_static/djipupper_photos/startup-position.png
    :align: center
    
    Startup position.


Step 7. Speed test (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Tune your reward function and domain randomization to improve Pupper's speed
#. Fastest Puppers will get extra credit!

DELIVERABLE: Test your policy during office hours

Resources
-----------

Wiring diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ../_static/wiring-diagram.png
    :align: center
    
    Wiring diagram.
