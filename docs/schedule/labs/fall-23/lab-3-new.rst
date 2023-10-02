Lab 3: Copy Cat (Dog...)
=======================================================

*Goal: 1) Learn how to compute inverse kinematics 2) Use IK to create a mirroring setup.*

.. figure:: ../../../_static/lab3.jpg
    :align: center

Step 1. Code inverse kinematics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Implement ``cost`` in ``kinematics.h`` as the squared-norm of the error between the position returned by ``FK(guess)`` and ``target_location``. 
#. Implement ``calculate_cost_gradient`` in ``kinematics.h`` using the finite differencing method we covered in lecture. A good perturbation size is small, like 0.001.
#. Implement ``inverse_kinematics`` in ``kinematics.h``. Play around with different step sizes, from 1 to 100, to see what works for you.
**Deliverable: Print out the last 10 costs of IK up to the thousanths decimal place. Do they decrease or increase?

Step 2. Test the consistency between forward kinematics and inverse kinematics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Implement ``test_ik`` in ``test_inv_kinematics.h``
#. Write a test by taking some reachable (x,y,z) point in space (think hard about what's reachable!), using your IK function to get the corresponding joint angles, then passing them to your FK function to retrieve the original (x,yz). These should match as long as the original point was reachable. 
#. Make sure the test passes before moving on
**Deliverable: What test point did you use? Write about why we are doing an FK -> IK consistency test rather than an IK -> FK test (2-3 sentences). Hint: Think about the robot leg configuration(s) **
.. The reason we're doing this IK -> FK consistency test and not a FK -> IK consistency test is that for any reachable point in space, the robot can flip its "elbow" joint up or down to get to that point in space, resulting in different joint angles.

Step 4. Almost there!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Implement ``loop`` in ``main.cpp``
#. Make sure that your test passes first
#. Calculate the cartesian end-effector position of the leg on bus2
#. Calculate the inverse kinematics of the leg on bus1 with the end effector position from the previous step
#. Calculate ``actuator_commands1`` using ``vectorized_pd`` to command the leg on bus1 given Kp and Kd gains provided
#. Hold both arms in the horizontal position and start the program
**Deliverable: What is the behavior of the two arms?       

Step 5. Put it together! Make your two robot arms match each other's end-effector positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Instead of passing the end effector position directly, add a 0.16 offset to the y position
#. Deploy to robot!
#. The result you should get is that the left arm and right arm are touching or very close at the end effector! You can put an object between the end-effectors and now you have a multi-robot manipulator!

.. #. Calculate the cartesian end-effector position of the right arm using FK.
.. #. Use this result to calculate the cartesian position of the right arm's end-effector relative to the base of the left arm.
.. #. Disable the right arm's torque by de-activating the motors in the right arm. [TODO link code line number]
.. #. Deploy to robot and sanity check the reported position
.. #. Figure out what to add/subtract from the right arm's position to get the corresponding position relative to the left arm.
.. #. Deploy to robot and sanity check that the position relative to the left arm is correct.
.. #. Use your IK to move the left arm to this position in the simulator. Check that the left arm doesn't freak out.
**Deliverable: Send a video of the arms roughly matching each other when you move them
Notes:
* The code is set up to control both arms, but currently we are commanding the second robot arm's actuators to stay at zero.

(Old) IK Lecture
------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/FvQ6NbqDR1U" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

