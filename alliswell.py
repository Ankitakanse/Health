import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="ALL IS WELL", page_icon="💪", layout="wide")
st.markdown("<h1 style='text-align: center; color: red;'>ALL IS WELL 💪</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>-Our Mision 24-Fit India</h6S>", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("legs.jpg")
img_lottie_animation = Image.open("bellyfat1.jpg")

# ---- HEADER SECTION ----

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Exercise", "Body Analysis","Posts","Contact"])

with tab1:
    with st.container():
       st.header("Health is wealth")
       #st.image("https://media.istockphoto.com/id/1280587810/photo/healthy-eating-exercising-weight-and-blood-pressure-control.jpg?b=1&s=612x612&w=0&k=20&c=VVrfTgmWB2kfCkCJbDJQ514mkmQcVQ9cQf44udxOkNA=", width=400)
       left_column, right_column = st.columns(2)
       
       with left_column:
           st.image("https://media.istockphoto.com/id/1280587810/photo/healthy-eating-exercising-weight-and-blood-pressure-control.jpg?b=1&s=612x612&w=0&k=20&c=VVrfTgmWB2kfCkCJbDJQ514mkmQcVQ9cQf44udxOkNA=", width=650)
          
       with right_column:
               st.write(
       """
       Health is a fundamental aspect of human life, and access to reliable health information is essential for maintaining good health. With the rise of the internet and social media, there is a vast amount of health-related information available online, but not all of it is trustworthy or accurate. In this context, there is a need for a centralized platform that provides credible and relevant health information to the public. 

  

The aim of this project is to create a platform that posts health-related information to help individuals make informed decisions about their health. The platform will include a wide range of topics, including nutrition, fitness, mental health, and disease prevention. The information will be provided in the form of articles, videos, and other multimedia content created by health experts and professionals. 

  

The platform will serve as a reliable and trustworthy source of health information for individuals seeking answers to their health-related queries. It will help individuals to improve their health literacy and make informed decisions about their health. By promoting health awareness, the platform aims to contribute towards a healthier & happier society. 

Our mission is 24 fit India. 
       """
   )
   

with tab2:
      with st.container():
       st.header("Crazy for Fitness")
       st.write("##")
       image_column, text_column = st.columns((1, 2))
       with image_column:
           st.image(img_lottie_animation)
       with text_column:
           st.subheader("30 Minute Exercise Routine To Lose Belly Fat")
           st.write(
               """
               Do you want to lose belly fat
               """
           )
           st.markdown("[Watch Video...](https://youtu.be/zXyfhoK-oKQ)")
           
      with st.container():
               image_column, text_column = st.columns((1, 2))
               with image_column:
                   st.image(img_contact_form)
               with text_column:
                   st.subheader("Best Leg Exercises [Quick Home Routine]")
                   st.write(
                       """
                       Want to lose leg fat
                       """
                   )
                   st.markdown("[Watch Video...](https://youtu.be/Opi9dfVfACc)")

with tab3:
    
    with st.container():
    
        
    # page title
            st.title('Body Mass Index')
        # page title
        
            st.image("https://api.parashospitals.com/uploads/2017/10/BMI.png", caption='BMI')
            st.latex(r'''
             a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
             \sum_{k=0}^{n-1} ar^k =
             a \left(\frac{1-r^{n}}{1-r}\right)
             ''')
            st.header(" Hello  World !! Do you know your BMI?")
        
            st.write("The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m²")
            display = ("male", "female")

            options = list(range(len(display)))

            value = st.selectbox("Gender", options, format_func=lambda x: display[x])

            st.write(value)
        
            age = st.slider('How old are you?', 17,135)
            st.write("I'm ", age, 'years old')
            Weight= st.slider('What is your weight?', 15,200)
            st.write("My weight is", Weight, ' kg')
            Height=st.slider('What is your height',1.0, 2.10)
            st.write("My height is", Height, 'm')
            if (st.button("Click HERE to get your BMI")):
                Weight/(Height*Height)
            BMI=Weight/(Height*Height)
            # if a person has a BMI less than 16.5
            if BMI< 16.5:
                st.write( 'The person is famine')
            # if a person's BMI is at least 16.5 but less than 18.5
            elif BMI>= 16.5 and BMI <  18.5:
                st.write( 'The person is underweight')
            # if a person's BMI is at least 18.5 but less than 25
            elif BMI>= 18.5 and BMI < 25.0:
                st.write( 'The person is healthy weight')
            # if a person's BMI is at least 25 but less than 30
            elif BMI>= 25.0 and BMI < 30.0:
                st.write( 'The person is overweight')
            # if a person's BMI is at least 30 but less than 35
            elif BMI>= 30.0 and BMI < 35.0:
                st.write('The person is moderate obesity')
            # if a person's BMI is at least 35 but less than 40
            elif BMI>= 35.0 and BMI < 40.0:
                st.write('The person is severe obesity')
            else:
                st.write(' The person is morbid obesity')
                

   
   



# ---- WHAT I DO ----
with tab4:
    with st.container():
        st.header("Take care of your Body It's the only place you have to live")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image("https://i0.wp.com/post.healthline.com/wp-content/uploads/2023/04/cheeseburger-732x549-thumbnail-732x549.jpg?w=420")
        with text_column:
            st.subheader("How Processed Meat and Refined Carbs Can Increase Your Risk of Type 2 Diabetes")
            st.markdown("[Link](https://www.healthline.com/health-news/how-processed-meat-and-refined-carbs-can-increase-your-risk-of-type-2-diabetes)")
        left_column, right_column = st.columns(2)
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image("https://i0.wp.com/post.healthline.com/wp-content/uploads/2023/04/female-laptop-stressed-732x549-thumbnail-732x549.jpg?w=420")
        with text_column:
            st.subheader("Stress Can Increase Your Biological Age. Here’s How You Can Reverse It")
            st.markdown("[Link](https://www.healthline.com/health-news/stress-can-increase-your-biological-age)")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("Check out this channel")
            st.write("[YouTube Channel >](https://www.youtube.com/@herbalife)")
            st.write("##")
            st.write(
                """
                On this channel you'll learn how to optimize your nutrition and upgrade your fitness routine so you can live a healthy life. Learn from top experts about the latest in health science. Follow along with step-by-step workout tutorials, recipe videos and healthy living tips.

Herbalife Nutrition is a global nutrition company that has helped people pursue a healthy, active life since 1980. Herbalife Nutrition, weight-management and personal care products are available in more than 90 countries. Our mission is to change people's lives by providing the best nutrition and weight-management products in the world and the best business opportunity in direct selling.

Disclaimer: This channel and its contents are intended to comply with laws and regulations of the country specified for each playlist although the information may be accessible to users outside those countries. Other countries may have laws, regulatory requirements and practices that differ from those in the specified countries.
                """
            )
            
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")



# ---- CONTACT ----
with tab5:
    with st.container():
        st.header("Get In Touch With Me!")
        st.write("##")
    
        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
        
        
        
        
        
