import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import time

# credentials
page_title = st.secrets['initialize']['page_title']
sidebar_title = st.secrets['initialize']['sidebar_title']
website = st.secrets['credits']['website']
name = st.secrets['credits']['name']
buymeacoffee = st.secrets['credits']['buymeacoffee']
api_key = st.secrets['api_key']
api_secret = st.secrets['api_secret']

# streamlit
st.set_page_config(
    '{}'.format(page_title),
    ':cyclone:',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        "Get Help": "https://hirawat.in",
        "About": "Boilerplate streamlit app",
    },
)
st.title(':star: ' + page_title)
st.sidebar.title(':cyclone: ' +  sidebar_title)

# footer & credits section
def footer():
    st.markdown('<div style="text-align: center">Made with ❤️ by <a href="{}">{}</a></div>'.format(website, name), unsafe_allow_html=True)
    with st.sidebar.expander("Credits", expanded=True):
        components.html(
            '{}'.format(buymeacoffee),
            height=80
        )


# widget

def main() -> None:
    # dashboard - buttons
    placeholder = st.empty()

    col1, col2, col3 = st.columns(3, gap="large")
    col1.button('On')
    col2.button('Off')
    col3.button('Trigger')
    st.markdown('---')

    # dashboard - values
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    # dashboard - charts
    with placeholder.container():
        st.subheader('FPGA live sensor data')
        co1, co2 = st.columns(2, gap="large")
        random_data = np.random.randn(20, 3)
        chart_data = pd.DataFrame(
            random_data,
            columns=['Temperature', 'Wind', 'Humidity'])

        with co1:
            st.line_chart(chart_data)    
            with st.expander("Raw Data"):
                st.experimental_show(random_data)

        with co2:
            sensor_data = [1, 5, 2, 6, 2, 1]
            st.bar_chart({"sensor_data": sensor_data})
            with st.expander("Raw Data"):
                st.experimental_show(sensor_data)
        # Sleep/update timer
        time.sleep(5)


    # sidebar
    st.sidebar.success('Demo connection successful', icon="✅")
    st.sidebar.info('Check ethernet/USB port', icon="ℹ️")
    st.sidebar.warning('FPGA/Micro-controller not connected', icon="⚠️")

    #footer()



if __name__ == '__main__':
    main()
