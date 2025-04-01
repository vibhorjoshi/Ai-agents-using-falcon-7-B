import streamlit as st
import time
import ai_agent
from bot_controller import BotController
from pick_place_task import PickPlaceTask
from langchain.tools import WebBrowser
from langchain.utilities import GoogleCalendar, Gmail
import b0RemoteApi  # CoppeliaSim Plus API

# Initialize CoppeliaSim Client
client = b0RemoteApi.RemoteApiClient('b0RemoteApi', 'b0RemoteApi')

# Web Browsing Agent
web_browser = WebBrowser()

# Google Services
google_calendar = GoogleCalendar(credentials_path="google_credentials.json")
gmail = Gmail(credentials_path="google_credentials.json")

def main():
    st.title("AI Agent, CoppeliaSim Plus & Automation Dashboard")

    # AI Agent Interaction
    st.header("AI Agent Interaction")
    user_input = st.text_input("Enter your prompt for Falcon-7B:", "Hello Falcon!")
    if st.button("Generate Response"):
        ai_agent_response = ai_agent.generate_response(user_input)
        st.write("**Falcon-7B Response:**", ai_agent_response)

    # Web Browsing Agent
    st.header("Web Browsing AI Agent")
    search_query = st.text_input("Enter search query:", "Latest AI research papers")
    if st.button("Browse Web"):
        search_results = web_browser.run(search_query)
        st.write("**Top Search Results:**", search_results)

    # Google App Automations
    st.header("Google Automations")
    if st.button("Fetch Calendar Events"):
        events = google_calendar.get_events()
        st.write("Upcoming Events:", events)

    if st.button("Check Unread Emails"):
        emails = gmail.get_unread_emails()
        st.write("Unread Emails:", emails)

    # CoppeliaSim Bot Controller
    st.header("CoppeliaSim Plus Bot Controller")
    if st.button("Move Bot Forward"):
        bot = BotController()
        bot.move_bot(2, 2)
        time.sleep(2)
        bot.stop_bot()
        bot.disconnect()
        st.success("Bot moved forward and stopped.")

    # Pick and Place Task
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

