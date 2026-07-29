import streamlit as st
import pandas as pd
from agents.travel_agent import plan_trip, get_trip_history
from orchestrator import get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="Travel Planning Assistant",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Travel Planning Assistant")
st.markdown("*AI-powered trip planning with specialized agents*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None
if "trip_results" not in st.session_state:
    st.session_state.trip_results = None

# Sidebar
with st.sidebar:
    st.header("🌍 Trips")
    
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            if st.button(f"✈️ {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                st.session_state.topic = t['name']
                st.session_state.trip_results = None
                st.rerun()
    else:
        st.info("No trips yet")
    
    st.markdown("---")
    st.header("🆕 New Trip")
    new_topic = st.text_input("Trip Name:")
    if st.button("Create Trip"):
        if new_topic:
            st.session_state.topic = new_topic
            st.session_state.trip_results = None
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Travel Agents")
    st.write("""
    - 🗺️ **Itinerary Builder** - Daily trip plans
    - 💰 **Cost Estimator** - Budget breakdown
    - 🎭 **Local Culture Coach** - Cultural insights
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"✈️ Trip: {st.session_state.topic}")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🗺️ Plan Trip", 
        "💰 Itinerary",
        "🎭 Culture",
        "📅 Timeline"
    ])
    
    with tab1:
        st.subheader("🗺️ Plan Your Trip")
        
        col1, col2 = st.columns(2)
        
        with col1:
            destination = st.text_input("📍 Destination", placeholder="e.g., Paris, Tokyo, New York")
            duration = st.number_input("📅 Trip Duration (days)", min_value=1, max_value=30, value=7)
        
        with col2:
            budget_options = ["💎 Luxury", "💰 Mid-range", "🎒 Budget", "Backpacker"]
            budget = st.selectbox("💵 Budget Level", budget_options)
            interests = st.text_area("🎯 Interests", placeholder="e.g., Food, History, Nature, Art, Adventure", height=100)
        
        if st.button("🗺️ Generate Trip Plan", type="primary"):
            if destination and interests:
                with st.spinner(f"🧠 Planning your trip to {destination}..."):
                    results = plan_trip(st.session_state.topic, destination, duration, interests, budget)
                    st.session_state.trip_results = results
                    st.success("✅ Trip plan complete!")
                    st.rerun()
            else:
                st.warning("Please fill in destination and interests")
    
    with tab2:
        st.subheader("💰 Trip Costs")
        
        if st.session_state.trip_results:
            cost = st.session_state.trip_results.get("cost", "")
            st.write(cost)
        else:
            st.info("Generate a trip plan first")
        
        st.markdown("---")
        st.subheader("🗺️ Daily Itinerary")
        
        if st.session_state.trip_results:
            itinerary = st.session_state.trip_results.get("itinerary", "")
            st.write(itinerary)
        else:
            st.info("Generate a trip plan first")
    
    with tab3:
        st.subheader("🎭 Local Culture Guide")
        
        if st.session_state.trip_results:
            culture = st.session_state.trip_results.get("culture", "")
            st.write(culture)
        else:
            st.info("Generate a trip plan first")
        
        st.markdown("---")
        st.subheader("💡 Cultural Tips")
        
        if st.session_state.trip_results:
            st.info("""
            **Quick Cultural Tips:**
            - 😊 Learn basic greetings in the local language
            - 👗 Dress respectfully, especially at religious sites
            - 📸 Ask before taking photos of people
            - 🍽️ Try local cuisine for authentic experiences
            - 🗣️ Be patient with language barriers
            """)
    
    with tab4:
        st.subheader("📅 Trip Timeline")
        
        if st.session_state.trip_results:
            # Display timeline
            st.markdown("### 🗺️ Itinerary Timeline")
            
            # Extract days from itinerary
            itinerary = st.session_state.trip_results.get("itinerary", "")
            
            if "Day 1" in itinerary:
                days = itinerary.split("Day")
                for i, day in enumerate(days[1:], 1):
                    with st.expander(f"📅 Day {i}"):
                        st.write("Day " + day)
            else:
                st.info("No detailed timeline available")
            
            # Export
            st.subheader("📥 Export Trip Plan")
            
            export_text = f"""=== TRIP PLANNING REPORT ===
Trip: {st.session_state.topic}

🗺️ ITINERARY:
{st.session_state.trip_results.get("itinerary", "N/A")}

💰 COST ESTIMATE:
{st.session_state.trip_results.get("cost", "N/A")}

🎭 CULTURAL GUIDE:
{st.session_state.trip_results.get("culture", "N/A")}

================================
Generated by Travel Planning Assistant
"""
            
            st.download_button(
                label="📥 Download Trip Plan",
                data=export_text,
                file_name=f"trip_plan_{st.session_state.topic}.txt",
                mime="text/plain"
            )
        else:
            st.info("Generate a trip plan first")

else:
    st.info("👈 Create a new trip or select an existing one")
    
    st.markdown("""
    ### ✈️ Travel Planning Assistant
    
    **AI-powered trip planning with specialized agents!**
    
    **How it works:**
    1. Create a trip
    2. Enter destination, budget, and interests
    3. Agents plan your perfect trip
    4. View itinerary, costs, and culture tips
    
    **The Travel Agents:**
    - 🗺️ **Itinerary Builder** - Daily trip plans
    - 💰 **Cost Estimator** - Budget breakdown
    - 🎭 **Local Culture Coach** - Cultural insights
    
    ### 🌍 Suggested Destinations:
    - 🗼 Paris, France
    - 🗽 New York, USA
    - 🏯 Tokyo, Japan
    - 🦘 Sydney, Australia
    - 🏛️ Rome, Italy
    - 🎡 Barcelona, Spain
    """)

# Footer
st.markdown("---")
st.caption("✈️ AthenaCore | Travel Planning Assistant | AI-Powered Trip Planning")