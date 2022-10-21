#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:59:18 2021

@author: Cheung Wan Ching
"""

def clear_screen(x):
    print("\n" * x)
    print('screen cleared')
    
def sperate_date_price(file_name):
    stock_data_1 = open(file_name, "r").read()
    for comma in ",":
        stock_data_1 = stock_data_1.replace(comma, " ")
    numbers = stock_data_1.split()
    numbers.pop(0)
    numbers.pop(0)
    #return numbers

    stock_date_list = []
    stock_price_list = []
    from datetime import datetime 
    for datas in numbers:
        if numbers.index(datas)%2 == 0:
           data_format_0 = "19"+str(datas)
           data_format_1 = datetime.strptime(data_format_0,'%Y%m%d').strftime('%Y-%m-%d')
           stock_date_list.append(str(data_format_1))
        else:
            stock_price_list.append(float(datas))
    return stock_date_list, stock_price_list

    
def get_data_list(stock_date_list, stock_price_list):
    data_list = []
    stime = str(input("enter the starting date:"))
    etime = str(input("enter the ending date:"))
    starting_point = stock_date_list.index(stime)
    ending_point = stock_date_list.index(etime)
    for i in range(starting_point,ending_point+1):
        data_list.append(float(stock_price_list[i]))                     
    return data_list
      
def mean(data_list):
    sum = 0.0
    for num in data_list:
        sum = sum + num
    return sum / len(data_list)


def median(data_list):
    data_list.sort()
    #print("sorted list: ", data_list)
    size = len(data_list)
    midPos = size // 2  #integer division
 
    if size % 2 == 0:   # evern elements
        median = (data_list[midPos] + data_list[midPos-1])/2
    else:
        median = data_list[midPos]
    return median

def up_and_down(data_list):
    up_and_down = data_list[-1]-data_list[-2]
    return up_and_down

def gain_or_loss(data_list):
    gain_or_loss = (data_list[-1]-data_list[-2]) / data_list[-2]*100
    return gain_or_loss

def all_detailed_mean_data(stock_price_list):
    mean_list = [0]

    first_data = [stock_price_list[0],stock_price_list[1]]
    mean_list.append(mean(first_data))
    
    for i in range(2,len(stock_price_list)):
        first_data.append(stock_price_list[i])
        mean_list.append(mean(first_data))
       
    return mean_list


def all_detailed_median_data(stock_price_list):
    median_list = [0]
    
    first_data = [stock_price_list[0],stock_price_list[1]]
    median_list.append(median(first_data))
    
    
    for i in range(2,len(stock_price_list)):
        first_data.append(stock_price_list[i])
        median_list.append(median(first_data))
        
    return median_list

def all_detailed_up_and_down_data(stock_price_list):
    up_and_down_list = [0]
    
    first_data = [stock_price_list[0],stock_price_list[1]]
    up_and_down_list.append(up_and_down(first_data))
    
    
    for i in range(2,len(stock_price_list)):
        first_data.append(stock_price_list[i])
        up_and_down_list.append(up_and_down(first_data))
        
    return up_and_down_list

def all_detailed_gain_or_loss_data(stock_price_list):
    gain_or_loss_list = [0]
    
    first_data = [stock_price_list[0],stock_price_list[1]]
    gain_or_loss_list.append(gain_or_loss(first_data))
    
    
    for i in range(2,len(stock_price_list)):
        first_data.append(stock_price_list[i])
        gain_or_loss_list.append(gain_or_loss(first_data))
        
    return gain_or_loss_list
    
def output_file(stock_date_list,stock_price_list,
                mean_list,median_list,
                up_and_down_list,gain_or_loss_list):
    create_file_name = input("Create a file name:")
    out_file = open(create_file_name, "w")
    out_file.write("Date,Close,Mean,Median,Up/Down,Gain/loss\n")
    for i  in range(len(stock_date_list)):
         out_file.write(str(stock_date_list[i]))
         out_file.write(",")
         out_file.write(str(stock_price_list[i]))
         out_file.write(",")
         out_file.write(str(mean_list[i]))
         out_file.write(",")
         out_file.write(str(median_list[i]))
         out_file.write(",")
         out_file.write(str(up_and_down_list[i]))
         out_file.write(",")
         out_file.write(str(gain_or_loss_list[i]))
         out_file.write("\n")                   
    out_file.close()

def main():
    print('This is my_tools module called')
    
        
if __name__ == '__main__' :
    main()
    