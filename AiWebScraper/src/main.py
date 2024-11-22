import streamlit as st
from scrape import scrape_website, extract_body, split_content, clean_content
from parse import parse_content

st.title("AI Web Scraper")
url = st.text_input("Enter URL")

if st.button("Scrape site"):
    if url:
        st.write("Scraping...")
        result = scrape_website(url)

        body_content = extract_body(result)
        cleaned_content = clean_content(body_content)

        st.session_state.content = cleaned_content

        with st.expander("Scraped Content"):
            st.text_area("Scraped Content", value=cleaned_content, height=300)

if "content" in st.session_state:
    parse_description = st.text_area("please describe the content",)

    if st.button("Submit"):
        if parse_description:
            st.write("Parsing...")

            parsed_content = split_content(st.session_state.content)
            result = parse_content(parsed_content, parse_description)
            st.write(result)
