import streamlit as st

# MBTI descriptions
descriptions = {
    "ISTJ": "You are the dependable organizer! ⛏️ You thrive in structured environments, excel in planning, and are a master at getting things done efficiently. Perfect for roles like project managers or accountants! 💼",
    "ISFJ": "The nurturing protector 🛏️‍♂️. You are empathetic, supportive, and detail-oriented. A wonderful fit for roles in healthcare, teaching 🏫, or social work! 💕",
    "INFJ": "Visionary and insightful 🤝🔮. You connect deeply with people, inspire change, and excel in counseling, writing 📝, or leading purposeful projects! 🌈",
    "INTJ": "Strategic mastermind 🧠. You see the big picture, create innovative solutions, and love problem-solving. Ideal for scientists ⚛️, engineers, or entrepreneurs! 🌟",
    "ISTP": "The pragmatic craftsman ⚖️. You love hands-on work, enjoy fixing things, and adapt quickly. Great as a mechanic, technician, or detective 🕵️‍♂️! 🛠️",
    "ISFP": "Creative and adventurous 🌌. You shine in artistic roles, love self-expression, and excel in design 🎨, music 🎵, or photography. 🌟",
    "INFP": "The idealistic dreamer 💡🧥. You are empathetic and driven by values, excelling in counseling, writing 📚, or activism! 🌿",
    "INTP": "The analytical thinker 🔬🔍. You are logical, curious, and inventive. Perfect for roles in programming, research, or academia! 🌐",
    "ESTP": "The energetic doer 🏆🚀. You thrive in action-packed roles, adapt quickly, and excel in sales, sports, or entrepreneurship! 💪🌈",
    "ESFP": "The life of the party 🎉🍻! You bring joy, excitement, and energy wherever you go. Perfect for performers, teachers 📚, or event coordinators! 📊",
    "ENFP": "The enthusiastic inspirer 🌟🌈! You love people, creativity, and inspiring change. Amazing in roles like coaching, marketing, or public speaking! 📺",
    "ENTP": "The curious debater 🔎📢! You enjoy challenges, generating ideas, and debating big questions. Perfect for inventors, consultants, or lawyers! 📚🌐",
    "ESTJ": "The efficient leader 👥✨. You value organization, rules, and results. A natural manager, executive, or law enforcement officer! 🌟🔒",
    "ESFJ": "The warm-hearted helper 🫶🌿. You love building relationships and creating harmony. Perfect as a nurse, teacher 🎓, or HR professional! 💖",
    "ENFJ": "The charismatic mentor 📝🎉. You inspire, motivate, and connect with others. Amazing in leadership, coaching, or public relations! 🌟",
    "ENTJ": "The bold commander 📈💪. You are confident, decisive, and visionary. A perfect fit for CEOs, strategists, or entrepreneurs! 🌐⚖️",
}

# Streamlit App
st.title("🌐 Discover Your MBTI Fit! 🎉")

# Dropdown for MBTI Selection
selected_mbti = st.selectbox(
    "Select your MBTI type to learn more about yourself! 🏆",
    list(descriptions.keys())
)

# Display the description
if selected_mbti:
    st.subheader(f"Your MBTI: {selected_mbti} 💥")
    st.write(descriptions[selected_mbti])
    st.balloons()  # For a fun animation!
