"""
Streamlit Cheat Sheet
App to summarise streamlit docs v0.86.0 for quick reference
There is also an accompanying png version
https://github.com/daniellewisDL/streamlit-cheat-sheet
v0.86.0 August 2021
Author: @daniellewisDL
Contributors: @arnaudmiribel | @akrolsmir | @nathancarter
"""

import streamlit as st
from pathlib import Path
import base64

# --- for simulated docs -- 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt



# Initial page config

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    

    
    option = st.beta_expander('Cheatsheet style')

    op = option.radio('select',['Descriptive Cheatsheet','Simulated Cheatsheet'],key='doc-style')

    if op == 'Descriptive Cheatsheet':
        st.markdown("<h2 style='text-align: center ; color: black; font-weight: bold; text-shadow: 2px 2px #808080; font-family: poppins;'>Descriptive Cheatsheet</h2>", unsafe_allow_html=True)
        st.markdown('***')
        cs_sidebar()
        cs_body()
    else:
        st.markdown("<h2 style='text-align: center ; color: black; font-weight: bold; text-shadow: 2px 2px #808080; font-family: poppins;;'>Simulated Cheatsheet</h2>", unsafe_allow_html=True)
        st.markdown('***') 
        cs_simulated()
        



    return None


def cs_display_text():
    data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
    
    st.markdown("<h5 style='text-align: center ; color: black;'>Rendered -- Display Text, Code & Data Sections</h5>", unsafe_allow_html=True)
    st.markdown('***')
    cols = st.beta_columns(2)
    cols[0].markdown('**Method**') 
    cols[1].markdown('**Render**')
    cols[0].markdown('***') # partition 
    cols[1].markdown('***') # partition 
    print('{}{}'.format(cols[0].write("**st.markdown**(`'_Markdown_'`)"),cols[1].markdown('_Markdown_') ))
    print('{}{}'.format(cols[0].write("**st.text**(`'Fixed width text'`)"),cols[1].text('Fixed width text')))
    print('{}{}'.format(cols[0].write("**st.latex**(`r''' e^{i\pi} + 1 = 0 '''`)"),cols[1].latex(r'''e^{i\pi} + 1 = 0''') ))
    print('{}{}'.format(cols[0].write("**st.write**(`'Most objects'`)"),cols[1].write('Most objects')))
    print('{}{}'.format(cols[0].write("**st.write**(`['st', 'is <', 3]`) "),cols[1].write(['st', 'is <', 3])))
    print('{}{}'.format(cols[0].write("$~~$"),'')) # 
    print('{}{}'.format(cols[0].write("$~~$"),'')) #  For formatting space
    print('{}{}'.format(cols[0].write("$~~$"),'')) # 
    print('{}{}'.format(cols[0].markdown('***'),cols[1].markdown('***')))
    print('{}{}'.format(cols[0].write("**st.title**(`'My title'`)"),cols[1].title('My title')))
    print('{}{}'.format(cols[0].write("$~~$"),'')) #  For formatting space
    
    print('{}{}'.format(cols[0].write("**st.header**(`'My header'`)"),cols[1].header('My header')))
    print('{}{}'.format(cols[0].write("**st.subheader**(`'My sub'`)"),cols[1].subheader('My sub')))
    print('{}{}'.format(cols[0].write("**st.code**(`'for i in range(8): foo()')`"),cols[1].code('for i in range(8): foo()')))
    print('{}{}'.format(cols[0].write("**st.dataframe**(`data`)"),cols[1].dataframe(data)))
    print('{}{}'.format(cols[0].write("$~~$"),'')) # 
    print('{}{}'.format(cols[0].write("$~~$"),'')) # For formatting space
    print('{}{}'.format(cols[0].write("**st.table**(`data.iloc[0:1]`)"),cols[1].dataframe(data.iloc[0:1])))
    print('{}{}'.format(cols[0].write("$~~$"),'')) # For formatting space
    print('{}{}'.format(cols[0].write("**st.json**(`{'foo':'bar','fu':'ba'}`)"),cols[1].json({'foo':'bar','fu':'ba'})))
    
    
    st.markdown('***')

    info = st.beta_expander('Direct References')
    info.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32 style='float:left; vertical-align:middle'>](https://docs.streamlit.io/en/stable/api.html#display-text) <small style='color:black; font-size:16px;'>Link to the Official Documentation of this Section </small>'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
    st.markdown('***')


def cs_display_charts():
    st.markdown("<h5 style='text-align: center ; color: black;'>Rendered -- Display Chart Section</h5>", unsafe_allow_html=True)
    st.markdown('***')
    chart_data = pd.DataFrame(np.random.randn(50, 3),columns=['a', 'b', 'c'])
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.markdown('** Streamlit Native Charts ** ')
    
    st.code("chart_data = pd.DataFrame(np.random.randn(50, 3),columns=['a', 'b', 'c'])")
    st.markdown('- **st.line_chart**(_`chart_data`_)')
    st.line_chart(chart_data)

    st.markdown('***')

    st.markdown('- **st.area_chart**(_`chart_data`_)')
    st.area_chart(chart_data)

    st.markdown('***')

    st.markdown('- **st.bar_chart**(_`chart_data`_)')
    st.bar_chart(chart_data)

    st.markdown('***')

    st.markdown('- **st.map**(_`data`_)')
    st.code("geo = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon']) # coordinates")    
    geo = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
    st.map(geo)
 
    st.markdown('***')

    st.markdown(' __External Plotting Libraries Integrated into Streamlit__')

    st.markdown(' - **Matplotlib (pyplot) Charts**')
    pyplot = '''
    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    
    '''
    
    st.code(pyplot)
    st.markdown('- **st.pyplot**(_`fig`_)')
    st.pyplot(fig)

    st.markdown('***')

    st.markdown("<h6 style='text-align: center ;'>Similarly, other plotting frameworks can be integrated into streamlit</h6>", unsafe_allow_html=True)
    st.markdown('***')
    info = st.beta_expander('Direct References')
    info.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32 style='float:left; vertical-align:middle'>](https://docs.streamlit.io/en/stable/api.html#display-charts) <small style='color:black; font-size:16px;'>Link to the Official Documentation of this Section </small>'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
    
    

def cs_display_media():
    st.markdown("<h5 style='text-align: center ; color: black;'>Rendered -- Display Media Section</h5>", unsafe_allow_html=True)
    st.markdown('***')

    st.markdown('**Image**')
    st.markdown("- **st.image**('_`path`_')")
    st.image('./brain.png',width=300)
    st.markdown('***')

    st.markdown('**Audio**')
    st.markdown("- **st.audio**(_`data`_)")
    audio_code = '''
     audio_file = open('./Media/Cornfield_Chase.wav', 'rb')
     audio_bytes = audio_file.read()
     st.audio(audio_bytes, format='audio/wav')
    '''
    st.code(audio_code)
    audio_file = open('./Media/Cornfield_Chase.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    st.markdown("<h6 style='text-align: center ;'>Source ~ Interstellar ✨( Cornfield Chase ) </h6>", unsafe_allow_html=True)
    
    st.markdown('***')
    st.markdown('**Video**')
    st.markdown("- **st.video**(_`data`_)")
    video_code = '''
    video_file = open('./Media/Star-6962.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    '''
    st.code(video_code)
    video_file = open('./Media/Star-6962.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("<h6 style='text-align: center ;'>Creator - fxxu, Source - Pixbay </h6>", unsafe_allow_html=True)
    st.markdown('***')
    
    info = st.beta_expander('Direct References')
    info.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32 style='float:left; vertical-align:middle'>](https://docs.streamlit.io/en/stable/api.html#display-media) <small style='color:black; font-size:16px;'>Link to the Official Documentation of this Section </small>'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
    
    st.markdown('***')

def cs_widgets():
    st.markdown("<h5 style='text-align: center ; color: black;'>Rendered -- Display Interactive Widgets Section</h5>", unsafe_allow_html=True)
    st.markdown('***')

    

    st.markdown("- **st.button**(_`'label'`_)")

    button_code = '''
    
    if st.button('Hit Me'): # True when Clicked on it
        # any functionality code
        st.balloons() # example

    '''
    
    st.code(button_code)
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Button _')
    if cols[1].button('Hit me'):
        st.balloons()
        
    
    st.markdown('***')

    st.markdown("- **st.checkbox**(_`'label'`_)")
    checkbox_code = '''

    if st.checkbox('check me out'):
        st.markdown('_Information_')


    '''

    st.code(checkbox_code)
    cols = st.beta_columns(2)
    cols[0].markdown('_ Rendered checkbox _ ')
    if cols[1].checkbox('check me out'):
            cols[1].markdown('-- _Information_')

    st.markdown('***')

    st.markdown("- **st.radio**(_`'label'`_, _`spec`_)")
    radio_code = '''

    option = st.radio('Radio', [1,2,3], key='radio')
    if option == 1:
        # do something 
    elif option == 2:
        # do something 
    else:
        # do something
        
    '''

    st.code(radio_code)
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Radio _')
    chosen = cols[1].radio('Radio', ['Japan','USA','United Kingdom'], key='radio')
    if chosen == 1:
        cols[1].markdown('Chosen - {}'.format(chosen))
    elif chosen == 2:
        cols[1].markdown('Chosen - {}'.format(chosen))
    else:
        cols[1].markdown('Chosen - {}'.format(chosen))

    st.markdown('***')

    st.markdown("- **st.selectbox**(_`'label'`_, _`spec`_)")
    selectbox_code = '''

    option = st.selectbox('Select', ['Japan','USA','United Kingdom'], key='selectbox')
    st.markdown('Selected ~ _{}_'.format(option))

    '''
    
    st.code(selectbox_code)
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Selectbox _')
    option = cols[1].selectbox('Select', ['Japan','USA','United Kingdom'], key='selectbox')
    cols[1].markdown('Selected ~ _{}_'.format(option))

    st.markdown('***')

    st.markdown("- **st.multiselect**(_`'label'`_, _`spec`_)")
    selectbox_code = '''

    option = st.multiselect('Select', ['Japan','USA','United Kingdom','India','Canada'], key='multiselect')
    st.markdown('Selected ~ _{}_'.format(option)) # returns a list

    '''
    
    st.code(selectbox_code)
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Multi-Select _')
    option = cols[1].multiselect('Select', ['Japan','USA','United Kingdom','India','Canada'], key='multiselect')
    cols[1].markdown('Selected ~ _{}_'.format(option))

    st.markdown('***')

    st.markdown("- **st.slider**(_`'label'`_, _`min_value=int`_, _`max_value=int`_)")
    st.code("st.slider('slide',min_value=0, max_value=10, key='slider')")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Slider _')
    value = cols[1].slider('Gauge',min_value=0, max_value=10, key='slider')
    cols[1].markdown('Slider Value ~ _{}_'.format(value))

    st.markdown('***')

    st.markdown("- **st.select_slider**(_`'label'`_, `options=_spec`_)")
    st.code("value = st.select_slider('Slide',options=[1,3,5,7,9,11,13],key='select_slider')")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Select-Slider _')
    value = cols[1].select_slider('Slide',options=[1,3,5,7,9,11,13],key='select_slider')
    cols[1].markdown('Slider Value ~ _{}_'.format(value))

    st.markdown('***')

    st.markdown("- **st.text_input**(_`'label'`_)")
    st.code("text = st.text_input('Enter Country Name',key='text_input')")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Text Input Field _')
    text = cols[1].text_input('Enter Country Name',key='text_input')
    cols[1].markdown('_Text_ : {}'.format(text))

    st.markdown('***')

    st.markdown("- **st.number_input**(_`'label'`_,`min_value=int`,`max_value=int`)")
    st.code("num = st.number_input('Number',min_value=10,max_value=20,key='number_input')")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Number Input Field _')
    num = cols[1].number_input('Number',min_value=10,max_value=20)
    cols[1].markdown('_Number_ : {}'.format(num))

    st.markdown('***')

    st.markdown("- **st.date_input**(_`'label'`_,_`min_value=datetime.date`_, _`max_value=datetime.date`_)")
    st.code("date = st.date_input('Select Date', key='date_input') # any-date ")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Date Input (Calendar) _')
    date = cols[1].date_input('Select Date', key='date_input')
    cols[1].markdown('_Date (YY-MM-DD)_ : {}'.format(date))

    st.markdown('***')
    
    st.markdown("- **st.time_input**(_`'label'`_)")
    st.code("date = st.time_input('Select Date', key='time_input') # any-time ")
    cols = st.beta_columns(2)
    cols[0].markdown(' _ Rendered Time Input _')
    time = cols[1].time_input('Select time', key='time_input')
    cols[1].markdown('_Date (hrs:mins:secs)_ : {}'.format(time))
    
    st.markdown('***')

    info = st.beta_expander('Direct References')
    info.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32 style='float:left; vertical-align:middle'>](https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets) <small style='color:black; font-size:16px;'>Link to the Official Documentation of this Section </small>'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
    
    st.markdown('***')
    
    



def cs_beta_widgets():

    st.markdown("<h5 style='text-align: center ; color: black;'>Rendered -- Widgets which are currently in BETA </h5>", unsafe_allow_html=True)
    st.markdown('***')
    

    st.markdown(" - **st.beta_expander**(_`label`_, expanded=_`False`_)")
    exp_code = '''

    exp = st.beta_xpander('Expander')
    exp.markdown('_Markdown Text_')
    exp.radio('Radio',['option1','option2'])

    '''
    st.code(exp_code)
    exp = st.beta_expander('Expander')
    exp.markdown('_Markdown Text_')
    exp.radio('Radio',['option1','option2'])
    
    st.markdown('***')

    st.markdown(" - **st.beta_columns**(_`spec`_)")
    col_code = '''

    spec = 3
    col0,col1,col2 = st.beta_columns(spec) # 3 - columns
    
    col0.markdown('_Column-0_')
    col1.markdown('_Column-1_')
    col2.markdown('_Column-2_')

    '''
    st.code(col_code)
    
    spec = 3
    col0,col1,col2 = st.beta_columns(spec) # 3 - columns
    
    col0.markdown('_Column-0_')
    col1.markdown('_Column-1_')
    col2.markdown('_Column-2_')

    st.markdown('***')

    info = st.beta_expander('Direct References')
    info.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32 style='float:left; vertical-align:middle'>](https://docs.streamlit.io/en/stable/api.html#lay-out-your-app) <small style='color:black; font-size:16px;'>Link to the Official Documentation of this Section </small>'''.format(img_to_bytes("logo.png")), unsafe_allow_html=True)
    
    
    



def cs_simulated():
    
    st.sidebar.header('Control Shelf')
    st.sidebar.markdown('***')
    
    types = ('Display Text & Data','Display Chart','Display Media','Display Widgets ✨','Beta Functionalities')
    context = st.sidebar.radio("Render Type",types,key='context-types')
    
    if context == types[0]:
        cs_display_text()
    
    elif context == types[1]:
        cs_display_charts()
    
    elif context == types[2]:
        cs_display_media()

    elif context == types[3]:
        cs_widgets()

    elif context == types[4]:
        cs_beta_widgets()



    st.sidebar.markdown('***')
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>st.cheat_sheet v0.71.0 | Nov 2020</small>'''.format(img_to_bytes("brain.png")), unsafe_allow_html=True)
    st.sidebar.markdown('***')
    st.sidebar.markdown('''Designed by <small style='font-weight:light; color:#000000; font-family:courier;'>: r0han;</small> [<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](http://bit.ly/git-99) '''.format(img_to_bytes("knowledge.png")), unsafe_allow_html=True)
    
    
# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Streamlit cheat sheet')

    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/en/stable/api.html), as of [Streamlit v0.86.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__How to install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.markdown('Import convention')
    st.sidebar.code('>>> import streamlit as st')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
st.sidebar.<widget>
>>> a = st.sidebar.radio(\'R:\',[1,2])
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
    st.sidebar.markdown('[Beta and experimental features](https://docs.streamlit.io/en/0.86.0/api.html#beta-and-experimental-features)')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://github.com/daniellewisDL/streamlit-cheat-sheet) <small>st.cheat_sheet v0.86.0 | Aug 2021</small>'''.format(img_to_bytes("brain.png")), unsafe_allow_html=True)

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
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
* optional kwarg unsafe_allow_html = True
st.caption('This is a small text')
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
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
    ''')
    col2.write('Batch widgets together in a form:')
    col2.code('''
>>> with st.form(key='my_form'):
>>> 	text_input = st.text_input(label='Enter some text')
>>> 	submit_button = st.form_submit_button(label='Submit')
    ''')

    # Control flow

    col2.subheader('Control flow')
    col2.code('''
st.stop()
    ''')

    # Lay out your app

    col2.subheader('Lay out your app')
    col2.code('''
st.container()
st.columns(spec)
>>> col1, col2 = st.columns(2)
>>> col1.subheader('Columnisation')
st.expander('Expander')
>>> with st.expander('Expand'):
>>>     st.write('Juicy deets')
    ''')


    # Display code

    col2.subheader('Display code')
    col2.code('''
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')

    # Display progress and status

    col3.subheader('Display progress and status')
    col3.code('''
st.progress(progress_variable_1_to_100)
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

    col3.subheader('Placeholders, help, and options')
    col3.code('''
st.empty()
>>> my_placeholder = st.empty()
>>> my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
    ''')

    # Mutate data

    col3.subheader('Mutate data')
    col3.code('''
DeltaGenerator.add_rows(data)
>>> my_table = st.table(df1)
>>> my_table.add_rows(df2)
>>> my_chart = st.line_chart(df1)
>>> my_chart.add_rows(df2)
    ''')

    # Optimize performance

    col3.subheader('Optimize performance')
    col3.code('''
@st.cache
>>> @st.cache
... def foo(bar):
...     # Mutate bar
...     return data
>>> # Executes d1 as first time
>>> d1 = foo(ref1)
>>> # Does not execute d1; returns cached value, d1==d2
>>> d2 = foo(ref1)
>>> # Different arg, so function d1 executes
>>> d3 = foo(ref2)
    ''')

    # Store data across reruns
    col3.subheader('Store data across reruns')
    col3.code('''
st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)
    ''')

    return None

# Run main()

if __name__ == '__main__':
    main()
