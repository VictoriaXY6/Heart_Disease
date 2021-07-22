import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

def generate_data():
    data = pd.read_csv('webapp/dataset/leading_cause_death.csv')
    # change any x value in DEATHS, any * or x value in AADR, any United States in STATE and all causes in CAUSE_NAME to null value
    data=data.mask(data['DEATHS']=='x').fillna(data.mean())
    data=data.mask(data['AADR']=='*').fillna(data.mean())
    data=data.mask(data['AADR']=='x').fillna(data.mean())
    data=data.mask(data['STATE']=='United States').fillna(data.mean())
    data=data.mask(data['CAUSE_NAME']=='All Causes').fillna(data.mean())
    # then drop all of them
    data = data.dropna()
    # remember to convert the value from object type to float
    data['DEATHS'] = pd.to_numeric(data['DEATHS'])
    data['AADR'] = pd.to_numeric(data['AADR'])
    return data

# convert data into list
def process_data(data):
    data_list = []
    for row in data.itertuples():
        data_list.append(row)
    return data_list

# generate a line chart for data
def generate_line_chart(data):
    line_chart_data = data[['YEAR', 'CAUSE_NAME', 'DEATHS']].groupby(['YEAR', 'CAUSE_NAME'], as_index=False).sum()
    fig = px.line(line_chart_data, x="YEAR", y="DEATHS", color='CAUSE_NAME')
    update_layout(fig, 
                'Number of death causes from 1999 to 2013', 
                dict(orientation="h",yanchor="top",xanchor="center",y=-0.3,x=0.5))
    return pio.to_html(fig, full_html=False)

# generate a pie chart for data
def generate_pie_chart(data):
    pie_chart_data = data[['CAUSE_NAME', 'DEATHS']].groupby('CAUSE_NAME', as_index=False).sum()
    fig = go.Figure(data=[go.Pie(labels=pie_chart_data['CAUSE_NAME'],
                             values=pie_chart_data['DEATHS'])])
    update_layout(fig, 
                'Percentage in each Death Causes', 
                None)
    return pio.to_html(fig, full_html=False)

# update the layout of the chart
def update_layout(fig, title, legend):
    fig.update_layout(
        legend=legend,
        title_text=title,
        autosize=True,
    )


