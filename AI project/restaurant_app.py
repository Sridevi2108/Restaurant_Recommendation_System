import streamlit as st
from pyswip import Prolog
import os
import base64

# Add this function to load the background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            height: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function before setting the title
add_bg_from_local(os.path.join("images", "background.png"))

# Initialize Prolog and consult knowledge base using absolute path
prolog = Prolog()
prolog.consult(os.path.join(os.path.dirname(__file__), "restaurant_kb.pl"))

st.title("🍽️ Restaurant Recommendation System")

cuisine = st.selectbox("Cuisine:", ["north_indian", "south_indian", "italian", "continental", "arabic", "japanese", "chinese", "korean", "fast_food", "mexican"])
price = st.selectbox("Budget:", ["low", "medium", "high"])
city = st.selectbox("City:", ["chennai", "tirunelveli", "vellore", "thoothukudi", "erode", "salem", "hosur", "trichy", "coimbatore", "thanjavur", "karur", "madurai"])
ambience = st.selectbox("Ambience:", ["fine_dining", "casual", "rooftop", "family", "romantic"])
type_of_food = st.selectbox("Type:", ["veg", "nonveg", "veg_nonveg"])
min_rating = st.slider("Minimum Rating:", min_value=0.0, max_value=5.0, value=4.0, step=0.5)

if st.button("Find Restaurants"):
    query = f"restaurant(Restaurant, '{cuisine}', '{price}', '{city}', '{ambience}', '{type_of_food}', Rating, Image), Rating >= {min_rating}."
    try:
        results = list(prolog.query(query))
        if results:
            st.subheader("🍴 Recommended Restaurants:")
            for result in results:
                restaurant = result["Restaurant"]
                rating = result["Rating"]
                image_path = result["Image"]
                full_image_path = os.path.join(os.path.dirname(__file__), "images", os.path.basename(image_path))
                st.image(full_image_path, width=300)
                st.write(f"**{restaurant.replace('_', ' ').title()}** — Rating: ⭐ {rating}")
                st.markdown("---")
        else:
            st.warning("No restaurants found matching your criteria.")
    except Exception as e:
        st.error(f"Prolog Query Error: {e}")

if st.button("Explain System"):
    st.subheader("ℹ️ How the system works:")
    st.markdown("""
    This system recommends restaurants based on:
    - **Cuisine** (e.g., south_indian, chinese, italian)
    - **Budget** (`low`, `medium`, `high`)
    - **City** (e.g., Chennai, Coimbatore, Madurai)
    - **Ambience** (`casual`, `fine_dining`, `rooftop`, etc.)
    - **Type** (`veg`, `nonveg`, or both)
    - **Minimum Rating** (slider from 0 to 5 stars)
    """)
