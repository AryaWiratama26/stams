import math
from typing import List, Union, Literal

data_type = Union[int, float]

def mean(data: List[data_type]) -> float:
    total = 0
    for i in data:
        total += i
        
    mean_val = total / len(data)

    return mean_val

def median(data: List[data_type]) -> float:
    
    data.sort()

    n = len(data)
    
    if n % 2 == 1:
        median_index = (n - 1) // 2
        median_val = data[median_index]

    else:
        index_1 = (n // 2) - 1
        index_2 = n // 2
        
        median_val = (data[index_1] + data[index_2]) / 2
        

    
    return median_val
    
    

def variance(data: List[data_type], def_var: Literal['s', 'p'] ='s') -> float:
    mean_of_data = mean(data=data)

    if def_var == 's':
        x = (len(data) - 1)
    elif def_var == 'p':
        x = len(data)
        

    total = 0
    for i in range(len(data)):
        total += (data[i] - mean_of_data)**2
        
        
    variance_val = total / x
    
    
    return variance_val

def std(data: List[data_type]) -> float:
    con_to_variance = variance(data=data)

    std_val = math.sqrt(con_to_variance)


    return std_val

def ranges(data: List[data_type]) -> float:
    
    max_val = max(data)
    min_val = min(data)

    range_val = max_val - min_val

    return range_val


