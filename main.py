import streamlit as st
import ai_agent
from bot_controller import BotController
from pick_place_task import PickPlaceTask
import time

def main():
    st.title("AI Agent and CoppeliaSim Controller")
    
    # AI Agent Interaction
    st.header("AI Agent Interaction")
    user_input = st.text_input("Enter your prompt for Falcon-7B:", "Hello Falcon!")
    if st.button("Generate Response"):
        ai_agent_response = ai_agent.generate_response(user_input)
        st.write("**Falcon-7B Response:**", ai_agent_response)
    
    # CoppeliaSim Bot Control
    st.header("Bot Controller")
    if st.button("Move Bot Forward"):
        bot = BotController()
        bot.move_bot(2, 2)
        time.sleep(2)
        bot.stop_bot()
        bot.disconnect()
        st.success("Bot moved forward and stopped.")
    
    # Pick-and-Place Task
    st.header("Pick and Place Task")
    if st.button("Execute Pick and Place"):
        task = PickPlaceTask()
        task.pick_object('gripper', 'box')
        time.sleep(2)
        task.place_object('drop_zone')
        task.disconnect()
        st.success("Pick and Place task executed successfully.")

if __name__ == "__main__":
    main()
