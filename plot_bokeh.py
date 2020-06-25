# https://towardsdatascience.com/beautiful-and-easy-plotting-in-python-pandas-bokeh-afa92d792167

import numpy as np
import pandas as pd
import pandas_bokeh

df = pd.DataFrame({
    'Year': np.arange(2010, 2020),
    'Category-A': np.random.uniform(9000, 15000, 10),
    'Category-B': np.random.uniform(9000, 15000, 10),
    'Category-C': np.random.uniform(9000, 15000, 10)
})

pandas_bokeh.output_notebook()

df.plot_bokeh(
    kind='bar',
    x='Year',
    y=['Category-A', 'Category-B', 'Category-C'],
    xlabel='Category',
    ylabel='Annual Sales',
    title='Annual Sales by Category'
)

df.plot_bokeh.line(
    x='Year', 
    y=['Category-A', 'Category-B', 'Category-C'],
    figsize=(900, 500),
    ylim=(5000, 20000),
    zooming=False,
    panning=False
)