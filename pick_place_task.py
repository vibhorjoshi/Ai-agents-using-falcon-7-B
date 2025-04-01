import sim
import time

class PickPlaceTask:
    def __init__(self, ip='127.0.0.1', port=19997):
        self.client_id = None
        self.ip = ip
        self.port = port
        self.connect()
    
    def connect(self):
        sim.simxFinish(-1)
        self.client_id = sim.simxStart(self.ip, self.port, True, True, 5000, 5)
        if self.client_id != -1:
            print("Connected to CoppeliaSim for Pick and Place Task")
        else:
            raise ConnectionError("Failed to connect to CoppeliaSim")
    
    def pick_object(self, gripper, target):
        """Pick an object using the robotic gripper."""
        _, gripper_handle = sim.simxGetObjectHandle(self.client_id, gripper, sim.simx_opmode_blocking)
        _, target_handle = sim.simxGetObjectHandle(self.client_id, target, sim.simx_opmode_blocking)
        
        sim.simxSetObjectParent(self.client_id, target_handle, gripper_handle, True, sim.simx_opmode_oneshot)
        print("Object picked up")
    
    def place_object(self, target):
        """Release the object at the designated location."""
        _, target_handle = sim.simxGetObjectHandle(self.client_id, target, sim.simx_opmode_blocking)
        sim.simxSetObjectParent(self.client_id, target_handle, -1, True, sim.simx_opmode_oneshot)
        print("Object placed")
    
    def disconnect(self):
        sim.simxFinish(self.client_id)
        print("Disconnected from CoppeliaSim")

if __name__ == "__main__":
    task = PickPlaceTask()
    task.pick_object('gripper', 'box')
    time.sleep(2)
    task.place_object('drop_zone')
    task.disconnect()
