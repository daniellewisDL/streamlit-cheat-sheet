[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/master/app.py)

# Streamlit Cheat Sheet

App to summarise streamlit docs v1.8.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.8.0 April 2022

Author:
* @daniellewisDL : https://github.com/daniellewisDL

Contributors:
* @arnaudmiribel : https://github.com/arnaudmiribel
* @akrolsmir : https://github.com/akrolsmir
* @nathancarter : https://github.com/nathancarter

# Versioning
* Based on Streamlit 1.8.0
* Made with Python 3.8.5

# Requirements
A clean venv with just pip and then Streamlit

# Deployments
[Streamlit Cheat Sheet - Sharing for Streamlit](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/master/app.py)

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
st.camera_input("一二三,茄子!")
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
>>> col1, col2 = st.columns(2)
>>> col1.subheader('Columnisation')
st.expander('Expander')
>>> with st.expander('Expand'):
>>>     st.write('Juicy deets')
```


### Batch widgets together in a form:

```python
>>> with st.form(key='my_form'):
>>> 	text_input = st.text_input(label='Enter some text')
>>> 	submit_button = st.form_submit_button(label='Submit')
```


## Display code

```python
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
```


## Display progress and status

```python
>>> with st.spinner(text='In progress'):
>>>   time.sleep(5)
>>>   st.success('Done')

st.progress(progress_variable_1_to_100)
st.balloons()
st.snow()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
```


## Placeholders, help, and options

```python
# Replace any single element.
>>> element = st.empty()
>>> element.line_chart(...)
>>> element.text_input(...)  # Replaces previous.

# Insert out of order.
>>> elements = st.container()
>>> elements.line_chart(...)
>>> st.write("Hello")
>>> elements.text_input(...)  # Appears above "Hello".

st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
st.experimental_show(objects)
st.experimental_get_query_params()
st.experimental_set_query_params(**params)
```

## Mutate data

```python
# Add rows to a dataframe after
# showing it.
>>> element = st.dataframe(df1)
>>> element.add_rows(df2)

# Add rows to a chart after
# showing it.
>>> element = st.line_chart(df1)
>>> element.add_rows(df2)
```


## Optimize performance
### Legacy caching
```python
>>> @st.cache
... def foo(bar):
...   # Do something expensive in here...
...   return data
>>> # Executes foo
>>> d1 = foo(ref1)
>>> # Does not execute foo
>>> # Returns cached item by reference, d1 == d2
>>> d2 = foo(ref1)
>>> # Different arg, so function foo executes
>>> d3 = foo(ref2)
```

### Cache data objects
```python
>>> @st.experimental_memo
... def foo(bar):
...   # Do something expensive and return data
...   return data
# Executes foo
>>> d1 = foo(ref1)
# Does not execute foo
# Returns cached item by value, d1 == d2
>>> d2 = foo(ref1)
# Different arg, so function foo executes
>>> d3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear values from *all* memoized functions
>>> st.experimental_memo.clear()
```

### Cache non-data objects
```python
# E.g. TensorFlow session, database connection, etc.
>>> @st.experimental_singleton
... def foo(bar):
...   # Create and return a non-data object
...   return session
# Executes foo
>>> s1 = foo(ref1)
# Does not execute foo
# Returns cached item by reference, d1 == d2
>>> s2 = foo(ref1)
# Different arg, so function foo executes
>>> s3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear all singleton caches
>>> st.experimental_singleton.clear()
```

### Other key parts of the API
<small>[State API](https://docs.streamlit.io/en/stable/session_state_api.html)</small><br>
<small>[Theme option reference](https://docs.streamlit.io/en/stable/theme_options.html)</small><br>
<small>[Components API reference](https://docs.streamlit.io/en/stable/develop_streamlit_components.html)</small><br>
<small>[API cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)</small><br>

---