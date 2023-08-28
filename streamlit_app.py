import streamlit
import pandas
import requests # To display fruityvice API response
import snowflake.connector # bring in some code from the snowflake library added (snowflake-connector-python)

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#  pull the data into a dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Choose the Fruit Name Column as the Index, or the multiselect will only show number index on streamlit page
my_fruit_list = my_fruit_list.set_index('Fruit')

# Put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Choose a Few Fruits to Set a Good Example
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the filtered dataframe on the streamlit page
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# Connect with fruityvice API and display the response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response) # -> <Response [200]>
# streamlit.text(fruityvice_response.json()) # -> The json of API data

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to the screen as a table
streamlit.dataframe(fruityvice_normalized)

# Query Snowflake Trial Account Metadata 
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# Query Data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()
# Get All the Rows, Not Just One
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Add a Second Text Entry Box to Allow the End User to Add a Fruit to the List
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.text("Thanks for adding " + add_my_fruit)
# This will not work correctly, but just go with it for now
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")










