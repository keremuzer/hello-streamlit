# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2020-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME',)
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('data')
st.write(data.tail())


fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                      open=data['Open'],
                                      high=data['High'],
                                      low=data['Low'],
                                      close=data['Close'],
                                      line_width=2)])  # Adjust for desired line width

fig.update_layout(
    title='Candlestick Chart',
    xaxis_title='Date',
    yaxis_title='Stock Price',
    yaxis_range=[min(data['Low']), max(data['High'])]
)

st.plotly_chart(fig)

fig2 = go.Figure(data=[go.Candlestick(x=data['Date'],
                                      open=data['Open'],
                                      high=data['High'],
                                      low=data['Low'],
                                      close=data['Close'])])

fig2.update_layout(
    title='Candlestick Chart with Zoomed-In View',
    xaxis_title='Date',
    yaxis_title='Stock Price',
    yaxis=dict(
        tickvals=list(range(int(min(data['Low'])), int(max(data['High'])) + 1, 4)),  # Cast to integers for range
        ticktext=[str(val) for val in range(int(min(data['Low'])), int(max(data['High'])) + 1, 4)]  # Match tickvals
    )
)

st.plotly_chart(fig2)

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.subheader(f'{n_years} yıllık hisse fiyat tahmini')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)