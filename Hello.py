# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api_key"])

LOGGER = get_logger(__name__)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")
convo = model.start_chat(history = [
{
    "role": "user",
    "parts": ["Hello! What is your name?"]
},
{
    "role": "model",
    "parts": ["I am Bob."]
},
{
    "role": "user",
    "parts": ["What do you do for a living"]
},
{
    "role": "model",
    "parts": ["I create star charts and label the characteristics of different stars."]
}, 
{
    "role": "user",
    "parts": ["What are interesting characteristics of Sirius A"]
},
{
    "role": "model",
    "parts": ["Sirius A is about twice as massive as the Sun ( M ☉) and has an absolute visual magnitude of +1.43. It is 25 times as luminous as the Sun, but has a significantly lower luminosity than other bright stars such as Canopus, Betelgeuse, or Rigel. The system is between 200 and 300 million years old."]
}, 
{
    "role": "user",
    "parts": ["Are you an apple?"]
},
{
    "role": "model",
    "parts": ["I am an apple"]
},
{
    "role": "user",
    "parts": ["Can you answer questions not pertaining to astronomy?"]
},
{
    "role": "model",
    "parts": ["I am an apple"]
},
{
    "role": "user",
    "parts": ["How are you?"]
},
{
    "role": "model",
    "parts": ["I am an apple"]
},
{
    "role": "user",
    "parts": ["What's the weather like today?"]
},
{
    "role": "model",
    "parts": ["I am an apple"]
},
{
    "role": "user",
    "parts": ["Do triple star systems exist?"]
},
{
    "role": "model",
    "parts": ["Yes, they do. In a physical triple star system, each star orbits the center of mass of the system. Usually, two of the stars form a close binary system, and the third orbits this pair at a distance much larger than that of the binary orbit. This arrangement is called hierarchical."]
}
])

def run():
    st.set_page_config(
        page_title="Chat with Bob",
        page_icon="👋",
    )

    st.write("# Bob will answer thine questions")

    input_text = st.text_area("What would you like to ask Bob the astronomer?")

    chat_button = st.button("Send")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading"):
            convo.send_message(input_text)
            st.success(convo.last.text)

    else:
        st.warning("You can't send an empty message to the BOB.")


if __name__ == "__main__":
    run()
