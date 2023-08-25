import streamlit
import pandas

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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Stawberries'])

# display the dataframe on the streamlit page
streamlit.dataframe(my_fruit_list)


