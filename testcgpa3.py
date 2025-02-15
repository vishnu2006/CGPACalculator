import streamlit as st

# Title and description
st.title("CGPA and SGPA Calculator")
st.write("Enter your predicted CGPA for each subject:")

# Option to enter the current CGPA manually or use a slider
current_input_option = st.radio("Choose how to input your current CGPA:", ("Slider", "Manual Input"))

if current_input_option == "Slider":
    current = st.slider("What is your current CGPA?", 0.0, 10.0, step=0.1) * 64
else:
    current = st.number_input("Enter your current CGPA:", min_value=0.0, max_value=10.0, format="%.2f") * 41

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background: url("file:///C:/Users/vishn/Downloads/cool-wallpapers-v0-qm1v3yhghkvb1.jpg") no-repeat center center fixed;
        background-size: cover;
    }
    .subject-label {
        font-size: 18px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .fixed-right-middle {
        position: fixed;
        top: 50%;
        right: 2%;
        transform: translateY(-50%);
        width: 200px;
    }
    .circle {
        border-radius: 50%;
        color: white;
        text-align: center;
        padding: 40px;
        margin: 10px;
        font-size: 24px;
    }
    .stSlider .stSliderThumb {
        background: linear-gradient(90deg, red, green);
    }
    .stSlider .stSliderValue {
        background: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Subject inputs
subjects = [
    ("SPQT", 3), ("SSP", 3), ("DAA", 3), ("FML", 3), ("DAV", 3), ("EEA", 3),
    ("SPQT Lab", 1), ("Linux & LaTeX Lab", 1), ("DAA Lab", 1), ("FML Lab", 1), ("Upskill Course", 0.5)
]

summ = 0
for subject, credits in subjects:
    st.markdown(f'<p class="subject-label">{subject} (Credits: {credits})</p>', unsafe_allow_html=True)
    summ += st.slider(subject, 0, 10, step=1) * credits

# Calculate SGPA and CGPA
sgpa = summ / 22.5
cgpa = (summ + current) / 86.5

# Color settings for CGPA and SGPA
def get_color(value):
    if value < 6:
        return "#FF4C4C"  # Red
    elif value < 7:
        return "#FFA500"  # Orange
    elif value < 8:
        return "#FFD700"  # Yellow
    elif value < 9:
        return "#ADFF2F"  # Light Green
    else:
        return "#4CAF50"  # Green

sgpa_color = get_color(sgpa)
cgpa_color = get_color(cgpa)

# Display results
st.markdown(
    f"""
    <div class="fixed-right-middle">
        <div class="circle" style="background-color: {sgpa_color};">
            SGPA: {sgpa:.2f}
        </div>
        <div class="circle" style="background-color: {cgpa_color};">
            CGPA: {cgpa:.2f}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
