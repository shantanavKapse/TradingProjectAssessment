from django.shortcuts import render
import pandas as pd
import math

# Create your views here.
def index(request):
    if request.method == 'POST':
        timeframe = int(request.POST.get('timeframe'))
        csv_file = request.FILES.get('csv_file')
        df = pd.read_csv(csv_file)
        iters = math.ceil(df.shape[0]/timeframe)
        for i in range(iters):
            ini = i*timeframe
            test_df = df[ini:ini+timeframe]
            print(test_df)
    return render(request, 'index.html')