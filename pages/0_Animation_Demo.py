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

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
import openai

def generate_image(prompt):
    client = openai.OpenAI(api_key=st.secrets["openai_api_key"])
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    image_url = response.data[0].url
    return image_url

def image_gen() -> None:
    st.set_page_config(
        page_title="Image Generation",
        page_icon=""
    st.markdown("# Create Your Animal")
    st.sidebar.header("Image Generation")
    )

    st.write("#The artist will create your image")

    input_text = st.text_area("What would you like made?")

    run_button = st.button("Send")

    if run_button and input_text.strip() != "":
        with st.spinner("Loading"):
            image_url = generate_image(input_text)
            st.image(image_url)

    else:
        st.warning("You can't send an empty message to the artist.")

image_gen()

