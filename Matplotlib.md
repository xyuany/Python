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
```python
plt.legend(['legend'],
          frameon = False, # Control the frame of legend
          loc = (0.25,0.015) # location, Left-lower corner, 0 is 'best', tuple is coordinates
          )
```
```Python
plt.gca().fill_between(range(len(linear_data)), #Must contain x axis 
                       data1, data2, # y axis data
                       facecolor='blue', 
                       alpha=0.25)
```
## Plot with dates
```Python
dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
plt.plot(dates, data) # To have a date x-axis
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbNDA4MDk1MzIwLDEzNDYwOTE2ODksMTE5ND
c2MzA0LC05NDc5NDkyOTgsMjA5NzQ1Mzc5MiwxMjQ1OTA5MDMw
LC0xMTU3NjEzODY3LC0xMDQxMzgxODddfQ==
-->