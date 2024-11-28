import streamlit as st
# streamlit run c:\Users\vishn\Downloads\testcgpa3.py

# Title and description
st.title("CGPA and SGPA Calculator")
st.write("Enter your predicted CGPA for each subject:")

# Option to enter the current CGPA manually or use a slider
current_input_option = st.radio("Choose how to input your current CGPA:", ("Slider", "Manual Input"))

if current_input_option == "Slider":
    current = st.slider("What is your current CGPA?", 0.0, 10.0, step=0.1) * 41
else:
    current = st.number_input("Enter your current CGPA:", min_value=0.0, max_value=10.0, format="%.2f") * 41

# Custom CSS for styling subject names
st.markdown(
    """
    <style>
    .subject-label {
        font-size: 18px;
        font-weight: bold;
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
    </style>
    """,
    unsafe_allow_html=True
)

# Display each subject label and slider
st.markdown('<p class="subject-label">MSF (Credits: 3)</p>', unsafe_allow_html=True)
a = st.slider("MSF", 0, 10, step=1, help="Microprocessor Systems Fundamentals") * 3

st.markdown('<p class="subject-label">DLCA (Credits: 3)</p>', unsafe_allow_html=True)
d = st.slider("DLCA", 0, 10, step=1, help="Digital Logic and Computer Architecture") * 3

st.markdown('<p class="subject-label">Java (Credits: 3)</p>', unsafe_allow_html=True)
b = st.slider("Java", 0, 10, step=1, help="Java Programming") * 3

st.markdown('<p class="subject-label">OS (Credits: 3)</p>', unsafe_allow_html=True)
c = st.slider("OS", 0, 10, step=1, help="Operating Systems") * 3

st.markdown('<p class="subject-label">DS (Credits: 3)</p>', unsafe_allow_html=True)
e = st.slider("DS", 0, 10, step=1, help="Data Structures") * 3

st.markdown('<p class="subject-label">DBMS (Credits: 3)</p>', unsafe_allow_html=True)
f = st.slider("DBMS", 0, 10, step=1, help="Database Management Systems") * 3

st.markdown('<p class="subject-label">Java Lab (Credits: 1)</p>', unsafe_allow_html=True)
g = st.slider("Java Lab", 0, 10, step=1, help="Java Programming Lab") * 1

st.markdown('<p class="subject-label">DS Lab (Credits: 1)</p>', unsafe_allow_html=True)
h = st.slider("DS Lab", 0, 10, step=1, help="Data Structures Lab") * 1

st.markdown('<p class="subject-label">DBMS Lab (Credits: 1)</p>', unsafe_allow_html=True)
i = st.slider("DBMS Lab", 0, 10, step=1, help="Database Management Systems Lab") * 1

# Fixed value for MOOC NPTEL

st.markdown('<p class="subject-label">MOOC Course internship (Credits: 2)</p>', unsafe_allow_html=True)
j = st.slider("MOOC", 0, 10, step=1, help="MOOC Internship") * 2

# Calculate SGPA and CGPA
summ = a + b + c + d + e + f + g + h + i + j
sgpa = summ / 23
cgpa = (summ + current) / 64

# Color settings for CGPA and SGPA
def get_color(value):
    if value < 6:
        return "#FF4C4C"  # Red for low values
    elif value < 8:
        return "#FFA500"  # Orange for mid-range values
    else:
        return "#4CAF50"  # Green for high values

sgpa_color = get_color(sgpa)
cgpa_color = get_color(cgpa)

# Display results in a fixed right middle position with colored circles
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
