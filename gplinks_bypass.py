import time

import cloudscraper

from bs4 import BeautifulSoup

import streamlit as st

# =======================================

def gplinks_bypass(url: str):

    client = cloudscraper.create_scraper(allow_brotli=False)

    domain = "https://gplinks.co/"

    referer = "https://mynewsmedia.co/"

    vid = client.get(url, allow_redirects=False).headers["Location"].split("=")[-1]

    url = f"{url}/?{vid}"

    response = client.get(url, allow_redirects=False)

    soup = BeautifulSoup(response.content, "html.parser")

    inputs = soup.find(id="go-link").find_all(name="input")

    data = {input.get('name'): input.get('value') for input in inputs}

    time.sleep(10)

    headers = {"x-requested-with": "XMLHttpRequest"}

    bypassed_url = client.post(domain + "links/go", data=data, headers=headers).json()["url"]

    return bypassed_url

# Streamlit app

st.title("GPLinks Bypass")

# Input URL

url = st.text_input("Enter GPLinks URL")

# Bypass button

if st.button("Bypass"):

    if url:

        bypassed_url = gplinks_bypass(url)

        st.success(f"Bypassed URL: {bypassed_url}")

    else:

        st.warning("Please enter a GPLinks URL.")




 
 
