import sim
import time

class BotController:
    def __init__(self, ip='127.0.0.1', port=19997):
        self.client_id = None
        self.ip = ip
        self.port = port
        self.connect()
    
    def connect(self):
        sim.simxFinish(-1)
        self.client_id = sim.simxStart(self.ip, self.port, True, True, 5000, 5)
        if self.client_id != -1:
            print("Connected to CoppeliaSim")
        else:
            raise ConnectionError("Failed to connect to CoppeliaSim")
    
    def move_bot(self, left_velocity, right_velocity):
        """Controls bot movement by setting wheel velocities."""
        _, left_motor = sim.simxGetObjectHandle(self.client_id, 'left_motor', sim.simx_opmode_blocking)
        _, right_motor = sim.simxGetObjectHandle(self.client_id, 'right_motor', sim.simx_opmode_blocking)
        
        sim.simxSetJointTargetVelocity(self.client_id, left_motor, left_velocity, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.client_id, right_motor, right_velocity, sim.simx_opmode_streaming)
    
    def stop_bot(self):
        self.move_bot(0, 0)
    
    def disconnect(self):
        sim.simxFinish(self.client_id)
        print("Disconnected from CoppeliaSim")

if __name__ == "__main__":
    bot = BotController()
    bot.move_bot(2, 2)  # Move forward
    time.sleep(2)
    bot.stop_bot()
    bot.disconnect()
