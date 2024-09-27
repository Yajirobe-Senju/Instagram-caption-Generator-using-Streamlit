

*NOTE*: The following instructions are for VS code:

1. combine all the files in one folder.

Make sure you have Mini conda pre-installed and Python.

for that use:

`pip install python3`

and

download mini conda through this link : https://docs.anaconda.com/miniconda/

Make sure it is compatible with your version of OS

Open the files in VS code and the terminal within VS code, in there make sure to create a virtual environment using mini-conda. After that, copy the activation key and add it to the "Activation key" file, after removing the content the file already contains.

For streamlit open the terminal in VS code and after creating the Virtual environment; activate it as well and type in 

`pip install streamlit`

Secondly, open the "Main.py" file in VS code and make an extra .env file where you can add a free or paid API key you can add from sources of your choice, I used Gemini's key you may use any other. once that is done. make sure to add the api key into the .env file as so <Api variable name> = "Add your Api Key".

you may change the "GOOGLE_API_KEY" in the main.py to whatever variable name you gave your api key.

lastly, run the following command in the terminal `Streamlit run main.py`

Congratulations!! Your Chatbot is now working and is hosted for free. you may learn and make changes to the code as per your desire to make it work better. Best of luck and Thank you.
