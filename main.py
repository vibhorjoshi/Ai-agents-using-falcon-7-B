import ai_agent
from bot_controller import BotController
from pick_place_task import PickPlaceTask
import time

def main():
    # Run AI Agent
    print("\nRunning AI Agent...")
    user_input = "Hello Falcon!"
    ai_agent_response = ai_agent.generate_response(user_input)
    print("Falcon-7B Response:", ai_agent_response)
    
    # Control the Bot in CoppeliaSim
    print("\nConnecting to CoppeliaSim...")
    bot = BotController()
    print("Moving the bot forward...")
    bot.move_bot(2, 2)
    time.sleep(2)
    bot.stop_bot()
    bot.disconnect()
    
    # Execute Pick-and-Place Task
    print("\nExecuting pick-and-place task...")
    task = PickPlaceTask()
    task.pick_object('gripper', 'box')
    time.sleep(2)
    task.place_object('drop_zone')
    task.disconnect()
    
    print("\nAll tasks executed successfully!")

if __name__ == "__main__":
    main()
