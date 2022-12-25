import streamlit as st, pandas as pd

st.title("Hello World")
st.write("This is a test")

df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
st.write(df)

a = st.sidebar.slider("Select a range of values", 0, 100)

st.write("The current value is", a)

if st.button("Click me"):
    st.write("You clicked the button")
    
# inputs
name = st.text_input("Enter your name")
st.write("Hello", name)

st.number_input("Enter a number")
st.date_input("Enter a date")
st.time_input("Enter a time")
option = st.selectbox("Select a number", [1, 2, 3])
st.write("You selected", option)

# file uploader
uploaded_file = st.file_uploader("Choose a file")

chart_data = pd.DataFrame({"col1": [1, 2, 3], "col2": [10, 20, 30]})
st.line_chart(chart_data)

# map
map_data = pd.DataFrame({"lat": [37.76, 37.77, 37.78], "lon": [-122.4, -122.41, -122.42]})
st.map(map_data)

# progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)
    time.sleep(0.1)

# spinner
with st.spinner("Wait for it..."):
    time.sleep(5)
st.success("Done!")

# add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
    