## Time Series / Date functionality

All materials come from official tutorial [https://pandas.pydata.org/pandas-docs/version/0.19/timeseries.html](https://pandas.pydata.org/pandas-docs/version/0.19/timeseries.html)

Using the NumPy `datetime64` and `timedelta64` dtypes, we have consolidated a large number of features from other Python libraries like `scikits.timeseries` as well as created a tremendous amount of new functionality for manipulating time series data.

`pandas.to_datetime()` covert string type to date series.
`Series.dt.year`, `Series.dt.month`, `Series.dt.date` return year, month, date of `datetime64` series.  
`Series.dt.strftime(_*args_,`  return an array of formatted strings specified by date_format, eg: 
`df['Month-Day'] = df['Date'].dt.strftime("%m-%d")`
`df.drop()` to remove labelled axis, always one row/column.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNDgwNTU5ODEsMTMyNjU1MjQ3NSwtMT
gyMTUzOTc1NSwzNzM0MzI2ODUsLTk1NDA2NDY2OF19
-->