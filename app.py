# # _*_ coding: utf-8 _*_

# import logging
# from upbit import Upbit
# from flask import Flask, request, render_template

# app = Flask(__name__)
# upbit = Upbit()
# upbit.get_hour_candles('KRW-BTC')

# @app.route('/')
# def root():
#     market_list = request.args.getlist('market')
#     labels=[]
#     xlabels=[]
#     data_list=[]
#     if len(market_list) == 0:
#         return 'No market parameter'
#     for market in market_list:
#         candles=upbit.get_hour_candles(market)
#         if candles is None:
#             return 'invalid market: {}'.format(market)
#         label=market
#         xlabel=[]
#         dataset=[]
        
#         for candle in candles:
#             temp=candle['candle_date_time_kst']
#             temp=temp[11:13]
#             xlabel.append(temp)
#             dataset.append(candle['trade_price'])
#         xlabel=xlabel[::-1]
#         labels.append(label)
#         xlabels.append(xlabel)
#         data_list.append(dataset)
    
#     # for label in labels:
#     #     print(label, end=' ')
#     #     print(xlabels[i], end=' ')
#     #     print(data_list[i])
#     #     i+=1
#     # candles = upbit.get_hour_candles(market)
#     # if candles is None:
#     #     return 'invalid market: {}'.format(market)

#     # label = market
#     # xlabels = []
#     # dataset = []
#     # i = 0
#     # for candle in candles:
#     #     temp=candle['candle_date_time_kst']
#     #     temp=temp[11:13]
#     #     xlabels.append(temp)
#     #     dataset.append(candle['trade_price'])
#     #     i += 1
#     # print(xlabels)
#     # xlabels=xlabels[::-1]
#     #return render_template('chart.html', **locals())
#     print(locals())
#     return '1212'

# def main():
#     app.debug = True
#     app.run()


# if __name__ == '__main__':
#     main()
# _*_ coding: utf-8 _*_

import logging
from upbit import Upbit
from flask import Flask, request, render_template

app = Flask(__name__)
upbit = Upbit()
upbit.get_hour_candles('KRW-BTC')

@app.route('/')
def root():
    market = request.args.get('market')
    if market is None or market == '':
        return 'No market parameter'

    candles = upbit.get_hour_candles(market)
    if candles is None:
        return 'invalid market: {}'.format(market)

    label = market
    xlabels = []
    dataset = []
    i = 0
    for candle in candles:
        temp=candle['candle_date_time_kst']
        temp=temp[11:13]
        xlabels.append(temp)
        dataset.append(candle['trade_price'])
        i += 1
    print(xlabels)
    xlabels=xlabels[::-1]
    return render_template('chart.html', **locals())

def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()

