import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

def create_timeline_data(topic_log: list) -> pd.DataFrame:
    """Convert topic log to DataFrame for timeline visualization"""
    
    if not topic_log:
        return pd.DataFrame()
    
    data = []
    for entry in topic_log:
        data.append({
            "agent": entry["agent"],
            "content": entry["content"][:200] + "..." if len(entry["content"]) > 200 else entry["content"],
            "full_content": entry["content"],
            "timestamp": entry.get("timestamp", "Unknown"),
            "timestamp_dt": datetime.strptime(entry.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "%Y-%m-%d %H:%M:%S")
        })
    
    df = pd.DataFrame(data)
    if not df.empty:
        df = df.sort_values("timestamp_dt")
    return df

def render_timeline_cards(df: pd.DataFrame):
    """Render agent responses as visual timeline cards"""
    
    if df.empty:
        st.info("No timeline data available yet. Run some agents first!")
        return
    
    # Color mapping for agents
    agent_colors = {
        "Research Agent": "🔵",
        "Summarizer Agent": "🟢",
        "Devil's Advocate": "🔴",
        "Insight Agent": "🟣"
    }
    
    st.subheader("📊 Agent Collaboration Timeline")
    
    # Display cards in chronological order
    for idx, row in df.iterrows():
        agent = row["agent"]
        content = row["full_content"]
        timestamp = row["timestamp"]
        
        # Get emoji for agent
        emoji = agent_colors.get(agent, "🤖")
        
        # Create card
        with st.container():
            st.markdown(f"""
            <div style="
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                background-color: {'#f0f8ff' if idx % 2 == 0 else '#fafafa'};
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0;">{emoji} {agent}</h4>
                    <span style="color: #666; font-size: 0.9em;">🕐 {timestamp}</span>
                </div>
                <hr style="margin: 8px 0;">
                <p style="margin: 10px 0 0 0; white-space: pre-wrap;">{content}</p>
            </div>
            """, unsafe_allow_html=True)

def render_plotly_timeline(df: pd.DataFrame):
    """Render interactive Plotly timeline chart"""
    
    if df.empty:
        return
    
    # Create horizontal bar chart timeline
    fig = go.Figure()
    
    # Color mapping
    colors = {
        "Research Agent": "#2E86AB",
        "Summarizer Agent": "#A23B72",
        "Devil's Advocate": "#F18F01",
        "Insight Agent": "#6A994E"
    }
    
    # Add bars for each agent
    for agent in df["agent"].unique():
        agent_df = df[df["agent"] == agent]
        
        fig.add_trace(go.Bar(
            y=agent_df["timestamp"],
            x=[1] * len(agent_df),
            name=agent,
            marker_color=colors.get(agent, "#888"),
            text=agent_df["content"],
            textposition="inside",
            hovertext=agent_df["content"],
            hoverinfo="text",
            orientation='h',
            width=0.8
        ))
    
    fig.update_layout(
        title="Agent Collaboration Timeline",
        xaxis_title="Sequence",
        yaxis_title="Time",
        height=400,
        showlegend=True,
        barmode='group'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_agent_summary(df: pd.DataFrame):
    """Render summary statistics by agent"""
    
    if df.empty:
        return
    
    st.subheader("📈 Agent Contribution Summary")
    
    # Count contributions by agent
    agent_counts = df["agent"].value_counts()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Contributions", len(df))
    
    with col2:
        st.metric("Number of Agents", len(agent_counts))
    
    with col3:
        most_active = agent_counts.index[0] if not agent_counts.empty else "N/A"
        st.metric("Most Active Agent", most_active)
    
    # Bar chart of agent contributions
    st.bar_chart(agent_counts)
    
    # Agent statistics
    st.subheader("📋 Agent Activity Breakdown")
    agent_stats = []
    for agent, count in agent_counts.items():
        agent_stats.append({
            "Agent": agent,
            "Contributions": count,
            "Percentage": f"{(count/len(df)*100):.1f}%"
        })
    
    st.dataframe(pd.DataFrame(agent_stats))

def render_full_timeline(topic: str, topic_log: list):
    """Render complete timeline view"""
    
    df = create_timeline_data(topic_log)
    
    if df.empty:
        st.info(f"No timeline data for '{topic}'. Run some agents first!")
        return
    
    st.subheader(f"📜 Timeline: {topic}")
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["🃏 Card View", "📊 Chart View", "📈 Summary"])
    
    with tab1:
        render_timeline_cards(df)
    
    with tab2:
        render_plotly_timeline(df)
    
    with tab3:
        render_agent_summary(df)
    
    # Export options
    st.subheader("📥 Export Timeline")
    col1, col2 = st.columns(2)
    
    with col1:
        # Export as CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"timeline_{topic}.csv",
            mime="text/csv"
        )
    
    with col2:
        # Export as Text
        export_text = f"=== TIMELINE: {topic} ===\n"
        export_text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        export_text += "=" * 50 + "\n\n"
        
        for _, row in df.iterrows():
            export_text += f"[{row['timestamp']}] {row['agent']}\n"
            export_text += f"{row['full_content']}\n\n"
        
        st.download_button(
            label="📥 Download as Text",
            data=export_text,
            file_name=f"timeline_{topic}.txt",
            mime="text/plain"
        )