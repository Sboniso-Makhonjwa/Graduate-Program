import pandas as pd


import seaborn as sns
import matplotlib.pyplot as plt

from flask import Flask, send_file
from flask.templating import render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

# temp_updates = requests.get("https://run.mocky.io/v3/1fd068d7-cbb2-4ceb-b697-da7fcc1c520b").json()

temp_updates = {
   "forecasts":[
      {
         "date":"2020-11-05T22:00:00.000+0000",
         "temp":20.0,
         "humidity":30,
         "windSpeed":300,
         "safe":True
      },
      {
         "date":"2020-11-06T22:00:00.000+0000",
         "temp":40.0,
         "humidity":10,
         "windSpeed":300,
         "safe":True
      },
      {
         "date":"2020-11-07T22:00:00.000+0000",
         "temp":50.0,
         "humidity":30,
         "windSpeed":300,
         "safe":True
      },
      {
         "date":"2020-11-08T22:00:00.000+0000",
         "temp":90.0,
         "humidity":60,
         "windSpeed":6000,
         "safe":True
      },
      {
         "date":"2020-11-09T22:00:00.000+0000",
         "temp":770.0,
         "humidity":100,
         "windSpeed":8900,
         "safe":False
      },
      {
         "date":"2020-11-10T22:00:00.000+0000",
         "temp":220.0,
         "humidity":30,
         "windSpeed":3003,
         "safe":False
      }
   ],
   "lastUpdated": "2020-11-07T22:00:00.000+0000",
   "weatherStation": "NASA Mars North Weather Station",
}
temp_df = pd.DataFrame(temp_updates['forecasts'])
fig,ax=plt.subplots(figsize=(6,6))
ax = sns.set_style(style='darkgrid')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/table', methods=['GET', 'POST'])
def tables():
    temp_df['date'] = pd.to_datetime(temp_df['date'])
    last_updated = temp_updates['lastUpdated']
    weather_station = temp_updates['weatherStation']
    return render_template('tables.html',  
            tables=[temp_df.to_html(classes='data')], 
            titles=temp_df.columns.values,
            last_updated=last_updated,
            weather_station=weather_station
            )




if __name__ == '__main__':
    app.run(debug=True)