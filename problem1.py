# Lets say the input data is in boxData.csv
# import pandas library
import pandas as pd
import numpy as np
# Read Data
data = pd.read_csv('boxData.csv')

def group(df):
#     Iterate through the ID to get the grouping
    count = df.count()
    for i in df.ID:
        x_val = df[['ID' , 'x0', 'x1']].values
        y_val = df[['ID' , 'y0', 'y1']].values
        
        x0 = df[df['ID'] == i].x0 + 0.5
        x1 = df[df['ID'] == i].x1 + 0.5
        y0 = df[df['ID'] == i].y0 + 0.5
        y1 = df[df['ID'] == i].y1 + 0.5
        
        j = 0
        while (j < count ):
            if(x0 < x_val[j][1] or x1 < x_val[j][2] or x0 < x_val[j][2]  or x1 < x_val[j][1]):
                x0 = max(x_val[j][1] , x_val[j][2])
                x0 = x0 + 0.5
                
                j = j + 1
                
                df = df.drop(df['ID'] = j)
                x_val = np.delete(x_val, j)
            
            elif(x0 < x_val[j][1] or x1 < x_val[j][2] or x0 < x_val[j][2]  or x1 < x_val[j][1]):
                x1 = max(x_val[j][1] , x_val[j][2])
                x1 = x0 + 0.5
                
                j = j + 1
                
                df = df.drop(df['ID'] = j)
                x_val = np.delete(x_val, j)
            
            elif (y0 < y_val[j][1] or y1 < y_val[j][2] or y0 < y_val[j][2]  or y1 < y_val[j][1]) :
                y0 = max(y_val[j][1] , y_val[j][2])
                y0 = y0 + 0.5
                j = j + 1
                
                df = df.drop(df['ID'] = j)
                y_val = np.delete(y_val, j)
                
            elif (y0 < y_val[j][1] or y1 < y_val[j][2] or y0 < y_val[j][2]  or y1 < y_val[j][1]) :
                y1 = max(y_val[j][1] , y_val[j][2])
                y1 = y0 + 0.5
                j = j + 1
                
                df = df.drop(df['ID'] = j)
                y_val = np.delete(y_val, j)
                
            else :
                pass
        df[df['ID']==i].x0 = x0
        df[df['ID']==i].x1 = x1
        df[df['ID']==i].y0 = y0
        df[df['ID']==i].y1 = y1
    
    return df