## Time Series / Date functionality

All materials come from official tutorial [https://pandas.pydata.org/pandas-docs/version/0.19/timeseries.html](https://pandas.pydata.org/pandas-docs/version/0.19/timeseries.html)

Using the NumPy `datetime64` and `timedelta64` dtypes, we have consolidated a large number of features from other Python libraries like `scikits.timeseries` as well as created a tremendous amount of new functionality for manipulating time series data.

`pandas.to_datetime()` covert string type to date series.
`Series.dt.year`, `Series.dt.month`, `Series.dt.date` return year, month, date of `datetime64` series.  
`Series.dt.strftime(_*args_,`  return an array of formatted strings specified by date_format, eg: 
`df['Month-Day'] = df['Date'].dt.strftime("%m-%d")`

## Selecting/Indexing data
`df.drop()` to remove labelled axis, always one row/column.
`df.set_index()` Set the index
`df.reindex()`
`df.reset_index()` 
To change index but keep the old index
```python
df.reset_index().set_index('New Index')
```

## Group by: group, apply, aggreate
```Python
df/Series.groupby(by= mapping function / list of functions, dict, Series, or tuple, ['column names'], axis=0, sort= True)
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbODQ4ODk3ODk0LDk2NjE3ODE4Miw2MDIwOT
YyMTAsMTg0OTgyMDY1OSwxMzI2NTUyNDc1LC0xODIxNTM5NzU1
LDM3MzQzMjY4NSwtOTU0MDY0NjY4XX0=
-->