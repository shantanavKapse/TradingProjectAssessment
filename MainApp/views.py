from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pandas as pd
import math
import json


def index(request):
    if request.method == 'POST':
        candles = []
        timeframe = int(request.POST.get('timeframe'))
        csv_file = request.FILES.get('csv_file')
        df = pd.read_csv(csv_file)
        iters = math.ceil(df.shape[0]/timeframe)
        for i in range(iters):
            ini = i*timeframe
            test_df = df[ini:ini+timeframe]
            candle = {}
            candle['BANKNIFTY'] = test_df['BANKNIFTY'].iloc[0]
            candle['DATE'] = int(test_df['DATE'].iloc[0])
            candle['TIME'] = test_df['TIME'].iloc[0]
            candle['OPEN'] = float(test_df['OPEN'].iloc[0])
            candle['HIGH'] = float(test_df['HIGH'].max())
            candle['LOW'] = float(test_df['LOW'].min())
            candle['CLOSE'] = float(test_df['CLOSE'].iloc[-1])
            candle['VOLUME'] = float(test_df['VOLUME'].iloc[-1])
            candles.append(candle)
            # print(candle)
            # print('--------------')
        csv_file = default_storage.save(csv_file.name, csv_file)
        main_data = {"data": candles}
        json_file_name = csv_file[:-4]+'.json'
        default_storage.save(json_file_name, ContentFile(json.dumps(main_data, indent=4).encode('utf-8')))
        return redirect('result', json_file_name[:-5])
    return render(request, 'index.html')


def result(request, filename):
    return render(request, 'result.html', context={'file': filename})
