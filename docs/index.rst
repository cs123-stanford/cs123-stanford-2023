CS 123: A Hands-On Introduction to Building AI-Enabled Robots
#######################################################

.. figure:: _static/pupper-hero.jpg
    :align: center
    :alt: Pupper

    Pupper Robot

**2023 Teaching team:** 

* Instructors: `Prof. Karen Liu <https://tml.stanford.edu/people/karen-liu>`_ (Stanford CS), `Jie Tan <https://www.jie-tan.net/>`_ (Google DeepMind), `Stuart Bowers <https://handsonrobotics.org/>`_ (Hands-On Robotics)
* Co-Intructors: `Wenhao Yu <https://wenhaoyu.weebly.com/>`_ (Google DeepMind), `Tingnan Zhang <https://www.linkedin.com/in/tingnanzhang/>`_ (Google DeepMind)
* Head TAs: `Jaden Clark <https://jadenvc.github.io/>`_ (CS 2024), `Gabrael Levine <https://www.gabrael.io/>`_ (MS CS 2024)
* TAs: `Ankush Dhawan <https://www.linkedin.com/in/ankush-dhawan/>`_ (EE 2024), `Sydney Yan <https://www.linkedin.com/in/sydney-yan-35b97a1ab/>`_ (CS 2025), `Brandon Vu <https://www.linkedin.com/in/brandon-t-vu/>`_ (CS 2024)

**Overview:**

Welcome to the course page for Stanford's course in legged robots!

This course offers a hands-on introduction to AI-powered robotics. Unlike most introductory robotics courses, students will learn essential robotics concepts by constructing a quadruped robot from scratch and training it to perform real-world tasks such as navigation and command following. The course covers a broad range of topics critical to robot learning, including motor control, forward and inverse kinematics, system identification, simulation, and reinforcement learning. Through weekly labs, students will construct and program an agile robot quadruped named Pupper. In the final few weeks, students will undertake an open-ended project, such as training Pupper to perform agile movements, developing a vision system to allow Pupper to play fetch, or adapting large language models to enable Pupper’s ability to communicate with humans.

Researchers from Google DeepMind, Hands-On Robotics, and Toyota Research Institute will give lectures during the quarter on their work teaching robots new skills using reinforcement learning. 

*"Empowering robots with AI is essential to make them smart and useful in people's daily life. It is one of the most important research directions in both academia and industry. This class teaches the most relevant skills, gives students hand-on experiences, and prepares them for a career in the area of AI and robotics."* - Jie Tan, Staff Research Scientist at Google DeepMind

**Prerequisites:** CS107 (familiarity with the command line), MATH51/CME100 (understanding of gradients). Coding will be majority Python but some C++ (Arduino). No robotics experience necessary!!

**Grading:** Letter-Based

**Time:** Monday 1:30-4:20

**Location:** 50-52H

**Number of credits:** 3

**Enrollment capacity:** 20

**Waitlist:** 10

**Late Policy:** Late work will be accepted on a case by case basis. Since this class is very dependent on hardware builds, we highly discourage submitting work after the scheduled deadline. 

Schedule
===========

**Week 1** 9/25

No Class! School starts on a Tuesday (for some reason...), so we will have our first class on Monday week 2!

**Week 2** 10/2: Actuators and PID Control

* Lecture on BLDC robot actuators and low-level PID control of robot joints.
* :doc:`../schedule/labs/fall-23/lab-1` Introduction to Teensy microcontroller. Mechatronics assembly. Experimenting with PID to move BLDC actuators to desired angles. Moving three actuators simultaneously. 

**Week 3** 10/9: Forward Kinematics

* Lecture on forward kinematics of open-chain robots and applications.
* :doc:`../schedule/labs/fall-23/lab-2` Build 3-DOF leader-follower robot arms akin to a surgical robotic system.
* :doc:`.../schedule/labs/fall-23/lab-3` Program the robot to tell you the cartesian coordinates of the leg for any given position. Staying within a cartesian-space safety box with haptic feedback. 

**Week 4** 10/16: Inverse Kinematics

* Lecture on inverse kinematics of open-chain robots and applications
* :doc:`../schedule/labs/fall-23/lab-4` Program legs to move to desired locations using inverse kinematics. Finally, drawing images with a robot arm! Task-space impedance control if time allows.

**Week 5** 10/23: Model-Based Control, and Pupper Assembly

* Lecture on model-based gait control: e.g. theory behind gallop, walk, trot, etc and associated stability.
* :doc:`../schedule/labs/fall-23/lab-5` Program the robot to trot using open-loop task-space trajectories. Simulating the robot in PyBullet to design and test code before deploying in the real world.

**Week 6**: Reinforcement Learning

* Lecture on Reinforcement Learning for quadruped robots, and state-of-the-art RL simulation techniques
* :doc:`../schedule/labs/fall-23/lab-6` Students build full Pupper robot.

**Week 7** AI-enabled Quadrupeds, Robot Vision

* Lecture on Computer Vision for robotics
* Students brainstorm project ideas, do background research, and propose final project. 
* :doc:`../schedule/labs/fall-23/lab-7` Students build AI-enabled quadruped with vision

**Week 8** AI-enabled Quadrupeds, Large-language-models

* Lecture on Large-language-models for robotics
* :doc:`../schedule/labs/fall-23/lab-8` Students build AI-enabled quadruped integrated with LLMs.
* During this week, you will meet with TAs to review project final project proposals

**Week 9**

* Open lab time

**Week 10**

* Open lab time

**Week 11 (Finals Week)**

* Students finish final project and showcase to peers, faculty, and the greater robotics community.

**Week 11 (finals week)**

* Students upload code, documentation, and media so that future students / hobbyists can recreate their work.
* Play with robots!



.. toctree::
    :maxdepth: 2
    :caption: Course Schedule

    schedule/lectures/fall-23/week-1
    schedule/lectures/fall-23/week-2
    schedule/lectures/fall-23/week-3
    schedule/lectures/fall-23/week-4
    schedule/lectures/fall-23/week-5
    schedule/lectures/fall-23/week-6
    schedule/lectures/fall-23/week-7
    schedule/lectures/fall-23/week-8
    schedule/lectures/fall-23/week-9

.. toctree::
    :maxdepth: 1
    :caption: List of Labs

    schedule/labs/fall-23/labs_master

.. toctree::
    :maxdepth: 1
    :caption: References

    reference/references
    
