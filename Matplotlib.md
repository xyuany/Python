This is an study summary of Python matplotlib. Original link: [http://www.aosabook.org/en/matplotlib.html](http://www.aosabook.org/en/matplotlib.html)


# Overview of matplotlib Architecture
 `Figure` is the ***top-level matplotlib object*** that contains and manages all of the elements in a given graphic.
The architecture is logically separated into three layers, which can be viewed as a stack. Each layer that sits above another layer knows how to talk to the layer below it, but the lower layer is not aware of the layers above it. The three layers from bottom to top are: ***backend, artist, and scripting***.
## Backend Layer :  
Backend layer provides concrete implementations of the abstract interface classes.     
*  `FigureCanvas`  encapsulates the concept of a surface to draw onto (e.g. "the paper").   

the `FigureCanvas` implementation might simply set up a file-like object into which the default headers, fonts, and macro functions are defined, as well as the individual objects (lines, text, rectangles, etc.) that the `Renderer` creates.
-   `Renderer`  does the drawing (e.g. "the paintbrush")

`Renderer` is to provide a low-level drawing interface for putting ink onto the canvas.  
The original `Renderer` API was motivated by the GDK `Drawable` interface, which implements such primitive methods as `draw_point`, `draw_line`, `draw_rectangle`, `draw_image`, `draw_polygon`, and `draw_glyphs`

-   `Event`  handles user inputs such as keyboard and mouse events. Users can connect to these events to callback functions and interact with their figure and data.  

##  Artist Layer
The `Artist` hierarchy is the middle layer of the matplotlib stack, is the object that knows how to **take the `Renderer` (the paintbrush) and put ink on the canvas**. Everything you see in a matplotlib `Figure` is an `Artist` instance.   
The `Artist` doesn't know what kind of backend the renderer is going to draw onto (PDF, SVG, GTK+ DrawingArea, etc.) but it does know the `Renderer` API and will call the appropriate method (`draw_text` or `draw_path`). Since the `Renderer` has a pointer to its canvas and knows how to paint onto it, the `draw` method transforms the abstract representation of the `Artist` to colors in a pixel buffer, paths in an SVG file, or any other concrete representation.

There are two types of `Artist`s in the hierarchy. _Primitive_ artists represent the kinds of objects you see in a plot: `Line2D`, `Rectangle`, `Circle`, and `Text`. _Composite_ artists are collections of `Artist`s such as the `Axis`, `Tick`, `Axes`, and `Figure`. For example, the `Figure` contains one or more composite `Axes` and the background of the `Figure` is a primitive `Rectangle`.

The most important composite artist is the **`Axes`**, which is where most of the matplotlib API plotting methods are defined. Not only does the `Axes` contain most of the graphical elements that make up the background of the plot—***the ticks, the axis lines, the grid, the patch of color which is the plot background***—it contains numerous helper methods that create primitive artists and add them to the `Axes` instance.  
## Scripting Layer (pyplot)  
The script using the API above works very well, especially for programmers, and is usually the appropriate programming paradigm when writing a web application server, a UI application, or perhaps a script to be shared with other developers.  
`ax = gca()` invokes the stateful machinery to "get current Axes" (each Python interpreter can have only one "current axes"). 

# Tutorials
Summary of [https://matplotlib.org/tutorials/index.html](https://matplotlib.org/tutorials/index.html)  

![../../_images/anatomy.png](https://matplotlib.org/_images/anatomy.png)

[`gca()`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca") returns the current axes (a [`matplotlib.axes.Axes`](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes "matplotlib.axes.Axes") instance), and [`gcf()`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf") returns the current figure ([`matplotlib.figure.Figure`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") instance).

*****
## Axes

`Axes` as a class and have lots of attributes, including ploting, axis/limits. The following list some useful attributes. 

`ax.invert_xaxis()`

Change x axis/y axis range: 
`plt.axis([x_start,x_end,y_start,y_end])`, `plt.xlim()`, `plt.ylim()`  
```python
plt.legend(['legend'],
          frameon = False, # Control the frame of legend
          loc = (0.25,0.015) # location, Left-lower corner, 0 is 'best', tuple is coordinates
          )
```
## Common Plot
### Shade
```Python
plt.gca().fill_between(range(len(linear_data)), #Must contain x axis 
                       data1, data2, # y axis data
                       facecolor='blue', 
                       alpha=0.25)
```

### Barplot
```python
plt.bar(x_lables, data, color=color
		yerr = staderr*1.96, # y axis error bar
		tick_label = x_lables, # x axis ticks
		capsize = 4) # cap size of error bar
```
### Heatmaps
```python
plt.hist2d(X, Y, bins=25)
# add a colorbar legend
plt.colorbar()
```
## Subplot
To create subplot. create 1 row, 2 column, with the first axes.
```python
plt.subplot(1, 2, 2,
			sharey=ax1) # Have fixed y axis with (1,2,1)

#To draw 2 vertical plots
# keywords passed to the GridSpec constructor used to create the grid the subplots are placed on)		
plt.subplots(2,gridspec_kw={'hspace': 0} )	#height reserved for space between subplots
 
# create a 3x3 grid of subplots
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
```
Create customlized subplot. Use [`GridSpec`](https://matplotlib.org/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec"). 
```python
import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(3, 3)
f3_ax1 = fig3.add_subplot(gs[0, :])
f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax5 = fig3.add_subplot(gs[-1, -2])
```
Then we could get the figure.  

![../../_images/sphx_glr_gridspec_003.png](https://matplotlib.org/_images/sphx_glr_gridspec_003.png)

Add another subplot inside the plot
```python
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
```
*****


## Plot with dates
```Python
dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
plt.plot(dates, data) # To have a date x-axis
```
More information about tick and locator could read following:

Tick Formatter: [https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-formatters.html](https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-formatters.html)

Locator Formatter: [https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-locators.html](https://matplotlib.org/3.1.1/gallery/ticks_and_spines/tick-locators.html)

```python
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_minor_locator(mdates.DayLocator(bymonthday=15))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
```
To move x labels to center, could achieve by hide minor locator, it is a fake method ([https://matplotlib.org/3.1.1/gallery/ticks_and_spines/centered_ticklabels.html](https://matplotlib.org/3.1.1/gallery/ticks_and_spines/centered_ticklabels.html))
```python
for label in ax.xaxis.get_minor_ticks():
    label.tick1line.set_markersize(0)
    label.label1.set_horizontalalignment('center')
```
## Colors
Could read matplotlib tutorial for understanding.
```python
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

# Normalize is a class, when called, could normalize number
norm = Normalize(vmin=None, vmax=None) #return a scale
```
## Animation

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMzMjIyODk0MiwxNzQzMjk5MjkxLDEyMD
Q1MzkwMTAsMzI4Mjg1MzU4LC0xNDM0NTQ5ODgsLTMwMTcyNzY4
MywxODYwMjAxMDM2LDEzNTk2NTYwMiwtMTg2NTcyMjE0MiwtMT
EzNzAxNTAxNiwtODgwMDk5NTkzLC0xMjE0ODMxOTc2LDQyNjE2
NjgzMSwtODIyNTUzOTIwLDQwODA5NTMyMCwxMzQ2MDkxNjg5LD
ExOTQ3NjMwNCwtOTQ3OTQ5Mjk4LDIwOTc0NTM3OTIsMTI0NTkw
OTAzMF19
-->