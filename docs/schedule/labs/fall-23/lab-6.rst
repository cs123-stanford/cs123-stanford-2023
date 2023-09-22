Lab 6 - Hardware Assembly (WIP)
=======================================

.. contents:: :depth: 2

These instructions assume you are running Mac or Linux. If you have Windows 10 or lower, we recommend dual-booting linux. If you have Windows 11, try using the Windows Linux Subsystem. Otherwise proceed at your own risk!

Step 1. Prepare the bottom PCB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Clone the simulator repository ``git clone https://github.com/jietan/puppersim.git``
#. Follow the instructions in the `System setup <https://github.com/jietan/puppersim#system-setup/>`_ and `Getting the code ready <https://github.com/jietan/puppersim#getting-the-code-ready/>`_ sections of the Puppersim README.md.

Step 2. Assemble the legs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Follow instructions at https://github.com/Nate711/puppersim/blob/main/puppersim/reacher/README.md to run the commands to train the policy.
#. Wait about 50 iterations until going to step 3 but leave it training

Step 3. Attach the legs to the body
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Follow instructions at https://github.com/Nate711/puppersim/blob/main/puppersim/reacher/README.md to run the policy.

Step 4. Attach legs to PCB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Follow instructions at https://github.com/Nate711/puppersim/blob/main/puppersim/reacher/README.md to deploy to your robot.

Step 5. Attach electronics bulkhead to PCB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Do your own mini project!

Some ideas:

* Teach the robot to trace out a specific shape in the air. (medium)
* Teach the robot to turn itself off by pressing its power button. (medium)
* Add a cube in the pybullet simulation and teach the robot to kick it. (hard)
* Turn off torque on the elbow or shoulder motor and make the robot learn to balance the arm vertically. (hard)

Step 6. Attach top PCB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Follow instructions at https://github.com/Nate711/puppersim/blob/main/puppersim/reacher/README.md to deploy to your robot.

(Old) RL Lecture
---------------------------------

https://share.icloud.com/photos/0836FiHhLJuCXCs9TyqSW8Ilw

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSOdXk8Tz55ZzrXGzIeHZUEigYQPUS2bPOIQPeFiRIXSRrVX7hqwXnC1yJnaZoH-uvJZ0OnK4JAW14o/embed?start=false&loop=false&delayms=60000" frameborder="0" width="600" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
