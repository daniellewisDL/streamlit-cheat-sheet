"""
Streamlit Cheat Sheet
App to summarise streamlit docs v0.71.0 for quick reference
There is also an accompanying png version
https://github.com/daniellewisDL/streamlit-cheat-sheet
v0.71.0 November 2020 Daniel Lewis and Austin Chen
"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.header('Streamlit cheat sheet')

    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.71.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__How to install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.markdown('Import convention')
    st.sidebar.code('import streamlit as st')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
st.sidebar.<widget>
a = st.sidebar.radio(\'R:\',[1,2])
    ''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/0.70.0/api.html#beta-and-experimental-features)')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>st.cheat_sheet v0.71.0 | Nov 2020</small>'''.format(img_to_bytes("brain.png")), unsafe_allow_html=True)

    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    # Magic commands

    col1, col2, col3 = st.beta_columns(3)

    col1.subheader('Magic commands')
    col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')

    # Display text

    col1.subheader('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header(My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
* optional kwarg unsafe_allow_html = True
    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
    ''')

    # Display charts

    col1.subheader('Display charts')
    col1.code('''
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)
st.map(data)
    ''')

    # Display media

    col1.subheader('Display media')
    col1.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

    # Display interactive widgets

    col2.subheader('Display interactive widgets')
    col2.code('''
st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')
    ''')
    col2.write('Use widgets\' returned values in variables:')
    col2.code('''
for i in range(int(st.number_input('Num:'))): foo()
if st.sidebar.selectbox('I:',['f']) == 'f': b()
my_slider_val = st.slider('Quinn Mallory', 1, 88)
st.write(slider_val)
    ''')

    # Control flow

    col2.subheader('Control flow')
    col2.code('''
st.stop()
    ''')

    # Lay out your app

    col2.subheader('Lay out your app')
    col2.code('''
st.beta_container()
st.beta_columns(spec)
col1, col2 = st.beta_columns(2)
col1.subheader('Columnisation')
st.beta_expander('Expander')
with st.beta_expander('Expand'):
    st.write('Juicy deets')
    ''')


    # Display code

    col2.subheader('Display code')
    col2.code('''
st.echo()
with st.echo():
    st.write('Code will be executed and printed')
    ''')

    # Display progress and status

    col3.subheader('Display progress and status')
    col3.code('''
st.progress(progress_variable_1_to_100)
st.spinner()
with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
    ''')

    # Placeholders, help, and options

    col3.subheader('Placeholders, help, and options')
    col3.code('''
st.empty()
my_placeholder = st.empty()
my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
    ''')

    # Mutate data

    col3.subheader('Mutate data')
    col3.code('''
DeltaGenerator.add_rows(data)
my_table = st.table(df1)
my_table.add_rows(df2)
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
    ''')

    # Optimize performance

    col3.subheader('Optimize performance')
    col3.code('''
@st.cache
@st.cache
def foo(bar):
    # Mutate bar
    return data
# Executes d1 as first time
d1 = foo(ref1)
# Does not execute d1; returns cached value, d1==d2
d2 = foo(ref1)
# Different arg, so function d1 executes
d3 = foo(ref2)
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()
