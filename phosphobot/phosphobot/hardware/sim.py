"""
Setup the simulation environment for the robot
"""

import os
import subprocess
import time

import pybullet as p
from loguru import logger


def simulation_init():
    """
    Initialize the pybullet simulation environment based on the configuration.
    """
    from phosphobot.configs import config

    if config.SIM_MODE == "headless":
        p.connect(p.DIRECT)
        p.setGravity(0, 0, -9.81)

        logger.debug("Headless mode enabled")

    elif config.SIM_MODE == "gui":
        # Start the PyBullet GUI in the current process. This avoids relying on
        # an external simulator (previously expected in simulation/pybullet),
        # making the GUI mode work out-of-the-box as long as an X-server is
        # available.

        p.connect(p.GUI)
        p.setGravity(0, 0, -9.81)
        logger.debug("GUI mode enabled (in-process)")

    else:
        raise ValueError("Invalid simulation mode")


def simulation_stop():
    """
    Cleanup the simulation environment.
    """
    from phosphobot.configs import config

    if p.isConnected():
        p.disconnect()
        logger.info("Simulation disconnected")

    if config.SIM_MODE == "gui":
        # Kill the simulation process: any instance of python 3.8
        subprocess.run(["pkill", "-f", "python3.8"])
