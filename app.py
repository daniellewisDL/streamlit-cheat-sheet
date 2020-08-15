"""
Streamlit Cheat Sheet
This somewhat simple app summarises the streamlit docs for quick reference
There is also an accompanying pdf version
https://github.com/daniellewisDL/streamlit-cheat-sheet
v1.1
"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config - note this is in beta


st.beta_set_page_config(
     page_title='Streamlit cheat sheet',
     layout="centered",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()
    cs_footer()
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
[streamlit.io](https://www.streamlit.io/)
\nThis is a summary of the [docs](https://docs.streamlit.io/en/stable/api.html)
\nI also recommend [streamlitopedia](https://pmbaumgartner.github.io/streamlitopedia/front/introduction.html)
    ''')

    st.sidebar.markdown('__How to install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.markdown('Import convention')
    st.sidebar.code('>>> import streamlit as st')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
st.sidebar.<widget>
>>> my_val = st.sidebar.text_input(\'I:\')
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
    st.sidebar.markdown('To access beta and experimental features')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')

    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    # Magic commands

    st.subheader('Magic commands')
    st.markdown('''Magic commands allow you to implicitly `st.write()`''')
    st.code('''
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'a', a
'dataframe:', data
    ''')

    # Display text

    st.subheader('Display text')
    st.code('''
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

    st.subheader('Display data')
    st.code('''
st.dataframe(data)
st.table(data.iloc[0:10]
st.json({'foo':'bar','fu':'ba'})
    ''')

    # Display charts

    st.subheader('Display charts')
    st.code('''
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

    st.subheader('Display media')
    st.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

    # Display interactive widgets

    st.subheader('Display interactive widgets')
    st.code('''
st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.beta_color_picker('Pick a color')
st.file_uploader('File uploader')
    ''')
    st.write('Use widgets\' returned values in variables:')
    st.code('''
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
    ''')

    # Control flow

    st.subheader('Control flow')
    st.code('''
st.stop()
    ''')

    # Display code

    st.subheader('Display code')
    st.code('''
st.echo()

>>> with st.echo():
>>>     # Code below both executed and printed
>>>     foo = 'bar'
>>>     st.write(foo)
    ''')

    # Display progress and status

    st.subheader('Display progress and status')
    st.code('''
st.progress(progress__variable_1_to_100)

st.spinner()

>>> with st.spinner(text='In progress'):
>>>     time.sleep(5)
>>>     st.success('Done')

st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
    ''')

    # Placeholders, help, and options

    st.subheader('Placeholders, help, and options')
    st.code('''
st.empty()

>>> my_placeholder = st.empty()
>>> my_placeholder.text('Replaced!')

st.help(pandas.DataFrame)

st.get_option(key)
st.set_option(key)

st.beta_set_page_config(layout='wide')
    ''')

    # Mutate data

    st.subheader('Mutate data')
    st.code('''
DeltaGenerator.add_rows(data)

>>> my_table = st.table(df1)
>>> my_table.add_rows(df2)

>>> my_chart = st.line_chart(df1)
>>> my_chart.add_rows(df2)
    ''')

    # Optimize performance

    st.subheader('Optimize performance')
    st.code('''
@st.cache

>>> @st.cache
... def foo(bar):
...     # Mutate bar
...     return data
...
>>> d1 = foo(ref1)
>>> # Executes as first time
>>>
>>> d2 = foo(ref1)
>>> # Does not execute; returns cached value, d1==d2
>>>
>>> d3 = foo(ref2)
>>> # Different arg, so function executes
    ''')

    return None

# Footer

def cs_footer():
    st.markdown('''<hr>''', unsafe_allow_html=True)
#    st.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=64 height=64>'''.format(img_to_bytes("brain.png")), unsafe_allow_html=True)
    st.markdown('''<small>Streamlit cheat sheet v1.1 | August 2020</small>
                <br><small>[https://github.com/daniellewisDL/streamlit-cheat-sheet](https://github.com/daniellewisDL/streamlit-cheat-sheet)</small>
                ''', unsafe_allow_html=True)

    return None

# Run main()

if __name__ == '__main__':
    main()
