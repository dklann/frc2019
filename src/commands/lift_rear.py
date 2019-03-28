#!/usr/bin/python3

from wpilib.command import Command

class LiftRear(Command):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.requires(self.robot.lift)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.lift.liftRear()

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return self.isTimedOut()

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.lift.lowerRear()

    def interrupted(self):
        """Called when another Command which requires one or more of the same
           subsystems is scheduled to run"""
        self.end()