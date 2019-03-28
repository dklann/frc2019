#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.punch import Punch
from commands.pull import Pull
#from commands.open_claw import OpenClaw
#from commands.close_claw import CloseClaw
from commands.move_arm_with_triggers import MoveArmWithTriggers
from commands.intake_cargo import IntakeCargo
from commands.cover_hatch import CoverHatch
from commands.lift_winch import LiftWinch
from commands.lower_winch import LowerWinch
from commands.punch_rear import PunchRear
from commands.lift_front import LiftFront
from commands.lift_rear import LiftRear
from commands.invert_front import InvertFront
#from commands.pull_rear import PullRear
from commands.eject_cargo import EjectCargo
from commands.park import Park
from commands.toggle_camera import ToggleCamera
#from commands.eject_cargo import EjectCargo
from wpilib.interfaces.generichid import GenericHID
from commands.left import Left
from commands.right import Right



from wpilib.buttons import JoystickButton
from wpilib import XboxController
import wpilib
from thresholds import TriggerButton

class OI:
    '''Operator Interface - all button assignments and other human interface elements
    '''

    def __init__(self, robot):
        '''The Constructor - assign Xbox controller buttons to specific Commands.
        '''

        print("In OI:__init__")

        robot.xbox0 = wpilib.XboxController(0)
        robot.xbox1 = wpilib.XboxController(1)

        
        #claw = JoystickButton(robot.xbox1, XboxController.Button.kY)
        intake = JoystickButton(robot.xbox1, XboxController.Button.kA)
        liftwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperRight)
        lowerwinch = JoystickButton(robot.xbox1, XboxController.Button.kBumperLeft)
        ejectcargo = JoystickButton(robot.xbox1, XboxController.Button.kX)
        park = JoystickButton(robot.xbox1, XboxController.Button.kB)
        #lift_front = JoystickButton(robot.xbox1, XboxController.Button.kB)
        lift_rear = JoystickButton(robot.xbox1, XboxController.Button.kY)
        left = JoystickButton(robot.xbox1, XboxController.Button.kBack)
        right = JoystickButton(robot.xbox1, XboxController.Button.kStart)
        invertfront = JoystickButton(robot.xbox1, XboxController.Button.kStickRight)

        triggerbutton = TriggerButton(robot.xbox0, .1)
        punch = JoystickButton(robot.xbox0, XboxController.Button.kY)
        hatch = JoystickButton(robot.xbox0, XboxController.Button.kX)
        camera = JoystickButton(robot.xbox0, XboxController.Button.kStart)

    

        triggerbutton.whenPressed(MoveArmWithTriggers(robot))
        intake.toggleWhenPressed(IntakeCargo(robot))
        ejectcargo.toggleWhenPressed(EjectCargo(robot))
        #claw.toggleWhenPressed(OpenClaw(robot))
        punch.whenPressed(Punch(robot))
        punch.whenReleased(Pull(robot))
        hatch.toggleWhenPressed(CoverHatch(robot))
        liftwinch.whileHeld(LiftWinch(robot))
        lowerwinch.whileHeld(LowerWinch(robot))
        #punchrear.whenPressed(PunchRear(robot))
        #punchrear.whenReleased(PullRear(robot))
        park.whileHeld(Park(robot))
        camera.whenPressed(ToggleCamera(robot))
        left.whileHeld(Left(robot))
        right.whileHeld(Right(robot))
        invertfront.toggleWhenPressed(InvertFront(robot))
        #lift_front.whileHeld(LiftFront(robot))
        lift_rear.whileHeld(LiftRear(robot))
        #park.whileHeld(Park(robot))
