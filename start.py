import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import csv

folder = 'data'
file_path = 'results/result.csv'
alfa = 8
beta = 0.75
#OPTIMAL ALFA = 4 AND BETA = 0.75 (QUICK;NOT ALWAYS ALL POINTS; ALWAYS GOOD POINTS)
#NOT OPTIMAL ALFA = 8 AND BETA = 0.75 (SLOWER;ALWAYS ALL POINTS; NOT ALWAYS ALL POINTS ARE GOOD (MORE THEN 5 POINTS)-->WHILE LOOP IN FIND FUNCTION)

def find_max(data, data_character,data_max,data_std):
    #data_border = data_mean + 3*data_std
    data_border = data_character+(data_max - data_character)/alfa
    i = 0
    result = []
    checked_points = []
    for point in data['volt']:
        i=i+1
        if(point>data_border):
            checked_points.append(i)
        else:
            if(len(checked_points)>0):
                max_c_point = checked_points[0]
                for c_point in checked_points:
                    if(data['volt'][c_point]>data['volt'][max_c_point]):
                        max_c_point = c_point
                if(data['volt'][max_c_point]>data_border+beta*data_std):
                    result.append(max_c_point)
                checked_points = []
    
    while (len(result)>5):
        min_point = result[0]
        j = -1
        for point in result:
            j=j+1
            if(data['volt'][min_point]>data['volt'][point]):
                min_point = point
        result.remove(min_point)
                
    return result 

def find_min(data, data_character ,data_min,data_std):
    #data_border = data_mean - 3*data_std
    data_border = data_character-(data_character-data_min)/alfa
    i = 0
    result = []
    checked_points = []
    for point in data['volt']:
        i=i+1
        if(point<data_border):
            checked_points.append(i)
        else:
            if(len(checked_points)>0):
                min_c_point = checked_points[0]
                for c_point in checked_points:
                    if(data['volt'][c_point]<data['volt'][min_c_point]):
                        min_c_point = c_point
                if(data['volt'][min_c_point]<data_border-beta*data_std):
                    result.append(min_c_point)
                checked_points = []

    while (len(result)>5):
        max_point = result[0]
        j = -1
        for point in result:
            j=j+1
            if(data['volt'][max_point]<data['volt'][point]):
                max_point = point
        result.remove(max_point)    
    return result 

def data_plot(name):
    df = pd.read_csv(folder+'/'+name+'.csv')
    df = df.drop(df.index[0])
    df.columns = ['second', 'volt']
    df['second'] = df['second'].apply(float)
    df['volt'] = df['volt'].apply(float)
    data_describe = df.describe()

    data_mean = data_describe['volt']['mean']
    data_std = data_describe['volt']['std']
    data_min = data_describe['volt']['min']
    data_max = data_describe['volt']['max']
    data_25 = data_describe['volt']['25%']
    data_75 = data_describe['volt']['75%']

    
    if(data_mean-data_min > data_max - data_mean ):
        result = find_min(df,data_25,data_min,data_std)
    else:
        result = find_max(df,data_75,data_max,data_std)
    if(len(result)!=5):
        print("BŁĄD!!!"+name+" len:" + str(len(result)))
    
    to_csv = [name,df['volt'][result[0]]/df['volt'][result[1]],df['volt'][result[1]]/df['volt'][result[0]]]

    temp =  result[0]
    first = False
    for x in result:
        if(first):
            to_csv.append(df['second'][x] - df['second'][temp] )
            temp = x
        first = True

    for x in result:
            to_csv.append(df['second'][x])
            to_csv.append(df['volt'][x])


    
    fig, ax = plt.subplots(figsize=(16,7))
    ax.plot(df['second'],
            df['volt'])

    
    ax.set_xlabel('second')
    ax.set_ylabel('volt')
    for x in result:
        plt.plot(df['second'][x], df['volt'][x], marker="o",markeredgecolor="red", markerfacecolor="red")
        
    plt.savefig('results/'+name+'.png') #zapisz wykres
    #plt.show()
    
    return to_csv

def main():
    data_to_csv = []
    data_to_csv.append(['file name', 'first/second', 'second/first',  'pt2-pt1', 'pt3-pt2', 'pt4-pt3', 'pt5-pt4', 'pt1_time', 'pt1_volt', 'pt2_time', 'pt2_volt', 'pt3_time', 'pt3_volt', 'pt4_time', 'pt4_volt', 'pt5_time', 'pt5_volt'])
    folder_path = Path(folder)
    files = [f.stem for f in folder_path.iterdir() if f.is_file()]
    files_num = len(files)
    i = 0
    for file in files:
        i = i+1
        data_to_csv.append( data_plot(file))
        print("Done: ",i,"/",files_num)

    print("CSV prepering...")
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_csv)

if __name__ == '__main__':
    main()