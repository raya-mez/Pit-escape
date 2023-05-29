"""Webots controller for the pit escape benchmark."""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

# Max possible speed for the motor of the robot.
maxSpeed = 8.72

# Configuration of the main motor of the robot.
pitchMotor = robot.getMotor("body pitch motor")
pitchMotor.setPosition(float('inf'))
pitchMotor.setVelocity(0.0)

# Configuration of gyro sensor
gyro = robot.getGyro("body gyro")
gyro.enable(timestep)

# At first we go forward.
pitchMotor.setVelocity(0.97*maxSpeed)
forward = True

while robot.step(timestep) != -1:
    # We check if the robot is still in movement. 
    gyroval = gyro.getValues()
    if gyroval[1] == 0:
        # If yes, then we switch directions.
        if forward:
            pitchMotor.setVelocity(-0.97*maxSpeed) 
        else:
            pitchMotor.setVelocity(0.97*maxSpeed)
        forward = not forward
