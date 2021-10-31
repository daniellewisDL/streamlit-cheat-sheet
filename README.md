[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/master/app.py)

[![Open in Heroku](https://github.com/daniellewisDL/quote-image-gen/blob/7f7baf425ef5df2f26eeda7373dcb775381cd1e4/heroku_badge_black_white.svg)](https://streamlit-cheat-sheet.herokuapp.com/)

# Streamlit Cheat Sheet

App to summarise streamlit docs v1.0.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.0.0 October 2021

Author:
* @daniellewisDL : https://github.com/daniellewisDL

Contributors:
* arnaudmiribel : https://github.com/arnaudmiribel
* akrolsmir : https://github.com/akrolsmir
* nathancarter : https://github.com/nathancarter
* epogrebnyak : https://github.com/epogrebnyak

# Versioning
* Based on Streamlit 1.0.0
* Made with Python 3.8.5

# Requirements
A clean venv with just pip and then Streamlit

# Deployments
[Streamlit Cheat Sheet - Streamlit Cloud](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/master/app.py)

[Streamlit Cheat Sheet - Heroku](https://streamlit-cheat-sheet.herokuapp.com/)

# Show me
![Streamlit Cheat Sheet](https://github.com/daniellewisDL/streamlit-cheat-sheet/blob/master/streamlit-cheat-sheet.png)

---

# Cheat sheet content

## Magic commands

```python
# Magic commands implicitly `st.write()`
''' _This_ is some __Markdown__ '''
a=3
'dataframe:', data
```


## Display text

```python
import streamlit as st

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

* optional kwarg unsafe_allow_html = True
```


## Display data

```python
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
```


## Display charts

```python
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
```

## Display media

```python
st.image('./header.png')
st.audio(data)
st.video(data)
```

## Display interactive widgets

```python
st.button('Hit me')
st.download_button('On the dl', data)
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
```

### Use widgets' returned values in variables:

```python
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
```

## Control flow

```python
st.stop()
```

## Lay out your app

```python
st.form('my_form_identifier')
st.form_submit_button('Submit to me')
st.container()
st.columns(spec)
col1, col2 = st.columns(2)
col1.subheader('Columnisation')
st.expander('Expander')
with st.expander('Expand'):
    st.write('Juicy deets')
```

### Batch widgets together in a form:

```python
with st.form(key='my_form'):
 	text_input = st.text_input(label='Enter some text')
	submit_button = st.form_submit_button(label='Submit')
```

## Display code

```python
st.echo()
with st.echo():
    st.write('Code will be executed and printed')
```

## Display progress and status

```python
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
```

## Placeholders, help, and options

```python
st.empty()
my_placeholder = st.empty()
my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
```

## Mutate data

```python
DeltaGenerator.add_rows(data)
my_table = st.table(df1)
my_table.add_rows(df2)
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
```

## Optimize performance

```python
@st.cache
>>> @st.cache
... def fetch_and_clean_data(url):
...     # Mutate data at url
...     return data
>>> # Executes d1 as first time
>>> d1 = fetch_and_clean_data(ref1)
>>> # Does not execute d1; returns cached value, d1==d2
>>> d2 = fetch_and_clean_data(ref1)
>>> # Different arg, so function d1 executes
>>> d3 = fetch_and_clean_data(ref2)
```

### Other key parts of the API

- [State API](https://docs.streamlit.io/en/stable/session_state_api.html)
- [Theme option reference](https://docs.streamlit.io/en/stable/theme_options.html)
- [Components API reference](https://docs.streamlit.io/en/stable/develop_streamlit_components.html)
- [API cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)
