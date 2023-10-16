Lab 5: How to Train Your Dog
========================

*Goal: Use RL to control your Pupper.*

Step 1. Set Up Virtual Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_static/gcp_setup.jpg
    :align: center

    Access your group's GCP instance

#. Log into GCP and find the gcp-robotics project
#. Start your machine, and SSH into the instance (using the 'ssh' button on the webpage shown in the image above)
#. Navigate to the directory "jvclark/rl/legged_gym". Here, you will be able to run the train.py script to train a policy, and play.py script to run the latest policy.
#. Also, make a note of the username shown in the ssh window (it should look something like USERNAME@instance). This will be used in generating SSH key in the steps below.

Step 2. VS Code SSH Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Video of VS Code Setup

#. Setup SSH key using `instructions <https://cloud.google.com/compute/docs/connect/create-ssh-keys>`_ 
#. Once your ssh key is created run ``cat /path/to/key.pub`` and copy the full ssh key. The format should be ssh-rsa keyvalue user.
#. Go to your instance, select edit, and add an SSH key.
#. Install the VS Code 'Remote - SSH' extension.
#. Press Cmd + Shift + P. Select "Connect to host". then "Configure SSH Hosts...". Open the ".../.ssh/config" file. Fill out GCP host config as shown in the image.

.. figure:: ../../../_static/ssh_setup.jpg
    :align: center

    Setup SSH access

#. Press Cmd + Shift + P again. Then select "Connect to Host". Press Cmd + O to open the rl/legged_gym repository.
#. You should now be able to edit your code in the legged_gym repo.

Step 3. Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the SSH window from Step 1.

Access the starter code using ``cd rl/legged_gym``

Switch to the correct branch using ``git checkout class``

Edit the base height reward function so that Puppper stands up. Access the height of the robot relative to the ground using ``self.root_states[:, 2].unsqueeze(1) - self.measured_heights``. The desired base height is defined in ``self.cfg.rewards.base_height_target``.

Write the  ``_reward_base_height`` function in ``pupper.py`` file so that pupper stands

Run your code. Enter the SSH window and ``cd rl/legged_gym``. Then run
``python legged_gym/scripts/train.py --task=pupper_stand --num_envs=2000 --max_iterations=500 --run_name='standup_test' --headless`` 
to train your policy. Check the policy at 250 iterations.

Hint: Make sure that the reward is positive. The code clips rewards at 0. To do so, you can subtract a base height penalty (based on the current state of Pupper relative to the target state) from a constant.

DELIVERABLE: Screen recording of stand up in simulation

Step 4. Deploy Stand High Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Transfer policy from virtual machine to local machine

#. Clone the puppersim repo onto your local machine using ``git clone https://github.com/jietan/puppersim.git``. This repository contains policy deployment code for transferring the policy trained in simulation to the phsyical hardware.
#. Navigate inside the puppersim repo and run ``pip install -e .`` Don't forget the "." at the end.
#. Move your file into the puppersim repo. You can find the policy you just trained in the logs folder of  ``legged_gym`` in VS code, and drag and drop it to your  ``puppersim`` directory on your local machine. From your local machine run ``scp -i /path/to/ssh/token  user@instance:~/path/to/model /path/to/puppersim`` to move the file to your puppersim directory.Ex.) ``scp -i /Users/jaden/Downloads/isaac-gym-jaden.pem ubuntu@ec2-13-57-117-122.us-west-1.compute.amazonaws.com:/home/ubuntu/rl/legged_gym/logs/Jun06-00-33-22_pupper_test1/model_700.pt ~/Downloads/puppersim``
#. In local puppersim repo, change the policy called in isaac_gym_policy.py (located under the puppersim folder) to your policy name (your .pt file)
#. Turn on and calibrate Pupper. 
#. Connect the Ethernet cable from your computer to Pupper
#. run your policy on Pupper using ``./deploy_to_robot.sh python puppersim/puppersim/isaac_gym_policy.py --run_on_robot``. Make sure you are aware of the cables in advance and are prepared for Pupper to behave unexpectedly.

DELIVERABLE: Video of stand-up in real
    

Step 5. Walking Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Write the  ``_reward_forward_velocity`` functions in ``pupper.py`` so that Pupper receives a positive reward for higher velocities. Make sure to set the max reward returned at ``self.forward_velocity_clip``.

#. Calculate the current forward distance from origin using ``self.root_states[:, 0] - self.env_origins[:, 0] -self.base_init_state[0]``.
#. Calculate speed using ``self.last_forward_distances`` and time since last step ``self.dt``
#. Clip the speed using ``self.forward_velocity_clip``.
#. Update ``self.last_forward_distances``
#. Return the reward

Write the ``_reward_torques`` function in ``pupper.py`` so that Puppers penalize

Edit the ``forward_velocity`` and ``torques`` scales in ``pupper_config.py``

Run 
``python legged_gym/scripts/train.py --task=pupper_flat --num_envs=2000 --max_iterations=1500 --run_name='running_test' --headless`` 
to train your policy. Check policy around every 250 iterations to analyze if you have chosen the correct coefficients.

Experiment with different reward coefficents until you are happy with the walking gait.

Deploy policy on Pupper, as in step 4. Be careful as the robot may behave erratically.

DELIVERABLE: What terms are included in your reward functions? What coefficeints did you use? How did you come up with these terms and what was their desired effect? Why might this policy perform poorly on the physical robot?

DELIVERABLE: How did the performance in simulation compare to the performance on the physical robot? What about hte simluation might not be accurate to the real world?

Step 6. Domain Randomization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the ``domain_rand`` ranges in ``pupper_config.py``. Experiment with different ranges until Pupper has similar performance in the real world, to in simulation.

DELIVERABLE: For 3 different terms that you randomized, what ranges or values did you select, and how did you choose them?

Step 7. Speed test (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Tune your reward function and domain randomization to improve Pupper's speed. You can use any reward function defined in legged_robot.py, or add your own.
#. Fastest Puppers will get extra credit!

DELIVERABLE: Test your policy during office hours

Resources
-----------
`Legged Gym Paper <https://arxiv.org/pdf/2109.11978.pdf>`_

`Learning Quadrupedal Locomotion Over Challenging Terrain <https://arxiv.org/abs/2010.11251>`_
