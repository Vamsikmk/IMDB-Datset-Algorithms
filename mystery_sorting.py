import pandas as pd
#import math
import os
#import glob
import csv
import heapq

import sys
sys.path.append("../Sorting_Algorithms")
from sorting_algos import merge_sort
# =============================================================================
# from sorting_algos import compare_helper
# =============================================================================


column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']

####################################################################################
# Donot Modify this Code
####################################################################################
class FixedSizeList(list):
    def __init__(self, size):
        self.max_size = size

    def append(self, item):
        if len(self) >= self.max_size:
            raise Exception("Cannot add item. List is full.")
        else:
            super().append(item)

####################################################################################
# Mystery_Function
####################################################################################
def Nullify_Function(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def Mystery_Function(file_path, memory_limitation, columns):
    chuncks_2000 = FixedSizeList(memory_limitation)
    #Empty Final Folder before starting the process
    Nullify_Function('Final')
    
    count =0
    total_count = 0
    no_of_files_present=0
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            no_of_files_present = no_of_files_present +1
            read_csv_file= open(os.path.join(file_path, file_name), "r", encoding="utf-8")
            csv_reader = csv.reader(read_csv_file)
            row_count = sum(1 for row in csv_reader)
            total_count += row_count
    size_of_dataframe = (total_count - no_of_files_present)//memory_limitation

    #This line of code generates a list of file names where each filename is of the form "Individual/Sorted_i.csv", where i ranges from 1 to size_of_dataframe+1.
    Individual_file_names = ["Individual/Sorted_{}.csv".format(i+1) for i in range(size_of_dataframe+1)]
    #each file in the list Individual_file_names and appends the resulting file object to the list csv_file_names
    csv_file_names = []
    for file_index in Individual_file_names:
        file = open(file_index, "r", encoding='utf-8')
        csv_file_names.append(file)
        #print(csv_file_names)
    #This code reads each file in the list csv_file_names and appends this object to the list chuncks_2000
    for chunk_index in csv_file_names:
        chunk_location = csv.reader(chunk_index)
        chuncks_2000.append(chunk_location)
        #print(chunk_location,count)
        
    #This code extracts the header row from each chunk in the list chuncks_2000 using the next() function, and appends each header to the list headers.
    headers = []
    for chunk in chuncks_2000:
        header = next(chunk)
        headers.append(header)
        #print(headers)
    current_chunk = []
    for chunk in chuncks_2000:
        row = next(chunk, None)
        count = count +1
        current_chunk.append(row) 
        #print(chuncks_2000)

        
    reached_end = [False] * len(Individual_file_names)
    
    #This code creates an output file with a header row in a directory named "Final"
    if not os.path.exists("Final"):
        os.makedirs("Final")
    Limit_counter = 0
    output_file_number = 1
    
    name_of_csv = "Final/Sorted_" + str(output_file_number) + ".csv"
    output_file = open(name_of_csv, "w", encoding='utf-8', newline="")
    output_writer = csv.writer(output_file)
    output_writer.writerow(headers[0])  
    
    def min_heapify(arr, n, i):
        count =0
        count = count +1
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
    
        if left < n and arr[i][0] > arr[left][0]:
            smallest = left
    
        if right < n and arr[smallest][0] > arr[right][0]:
            smallest = right
    
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            min_heapify(arr, n, smallest)

    heap = []
    for i, row in enumerate(current_chunk):
        if row is not None:
            heapq.heappush(heap, (row[1:], i))
            
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(heap, n, i)
        #count = count+1
        # print(count,n)
    #This code pops items from a heap until it is empty, writes each item to an output file.
    #creates a new output file when the memory limit is reached, while also updating the current chunk and checking for the end of each chunk
    while heap:
        row, ind_index = heapq.heappop(heap)
        output_writer.writerow(current_chunk[ind_index])
        Limit_counter += 1
        if Limit_counter % memory_limitation == 0:
            Limit_counter = 0
            output_file.close()
            output_file_number += 1
            output_file = open("Final/Sorted_" + str(output_file_number) + ".csv", "w", encoding='utf-8', newline="")
            output_writer = csv.writer(output_file)
            output_writer.writerow(headers[0])
    
        try:
            current_chunk[ind_index] = next(chuncks_2000[ind_index])
            if current_chunk[ind_index] is not None:
                heapq.heappush(heap, (current_chunk[ind_index][1:], ind_index))
        except StopIteration:
            current_chunk[ind_index] = None
            reached_end[ind_index] = True
        
    
        if any(not end for end in reached_end):
            continue
        else:
            break
    
    output_file.close()
    
    for file in csv_file_names:
        file.close()
    
####################################################################################
# Data Chuncks
####################################################################################
def data_chuncks(file_path, columns, memory_limitation):

        chunks_2000 = FixedSizeList(2000)
        Nullify_Function('Individual')
        # chuncks_2000=FixedSizeList(2000)
        df= pd.read_csv(file_path).applymap(lambda x: x.strip() if isinstance(x, str) else x)#.apply(lambda y: y.str.strip() if y.dtype == "object" else y)
        #df = pd.read_csv(file_path)# Load the imdb_dataset.csv dataset
        column_vals = [0]+ [df.columns.get_loc(column) for column in columns]
        # data = df.iloc[:,column_vals].values.tolist()
        size_of_dataframe = len(df)//memory_limitation
        #print(len(df),size_of_dataframe)
        if 'tconst' not in columns:
            x = ['tconst'] + columns
            #print(x)
        
        else:
            x=columns
        
        i=j=0
        while(j<=size_of_dataframe):
            #print(j)
            #file_name = "Individual/Sorted_" + str(j + 1)
            #chuck= df[i:i+memory_limitation]
            chunks_2000 = df.iloc[i:i+memory_limitation,column_vals].values.tolist()
            output_list = merge_sort(chunks_2000, column_vals)
            #print(output_list)
            chuck_data_frame = pd.DataFrame(output_list,columns=x)
            #print(data_frame)
            chuck_data_frame.reset_index(drop=True).to_csv("Individual/Sorted_" +str(j + 1)+".csv", index=False)
            j=j+1
            #print(j)
            i=i+memory_limitation
            
# =============================================================================
#          #chuck= df[i:i+memory_limitation]
#         data = df.iloc[:,column_vals].values.tolist()
#         output_list = merge_sort(data, column_vals)
#         #print(output_list)
#         chuck_data_frame = pd.DataFrame(output_list,columns=x)
#         #print(data_frame)
#         chuck_data_frame.reset_index(drop=True).to_csv("Final/imdb_Sorted_1.csv", index=False)
# =============================================================================

            
def test_code1(file_path,columns):
    merged_df = pd.DataFrame()
        
    original_df = pd.read_csv("imdb_dataset.csv")
    arr = merged_df.values.tolist()
    column_vals = list(range((len(columns)+1)))
    arr = merge_sort(arr,column_vals)    
       
    original_df = pd.read_csv(file_path+ "/imdb_Sorted_1.csv")
    actual_df = pd.read_csv(file_path+ "/combined.csv")
    df_sorted = original_df.sort_values(columns)
    temp = df_sorted.equals(actual_df)
    if temp == True:
        print("Sorted all 93 files successfully")
    else :
        print("better luck next time")

       
#Enable only one Function each from data_chuncks and Mystery_Function at a time

#Test Case 13
#data_chuncks('imdb_dataset.csv', ['startYear'], 2000)

#Test Case 14
#data_chuncks('imdb_dataset.csv', ['primaryTitle'], 2000)

#Test Case 15
# data_chuncks('imdb_dataset.csv', ['startYear','runtimeMinutes' ,'primaryTitle'], 2000)

#Test Case 13
#Mystery_Function("Individual", 2000, ['tconst', 'startYear','runtimeMinutes' ,'primaryTitle'])
#Mystery_Function("Individual", 2000, ['startYear'])

#Test Case 14
#Mystery_Function("Individual", 2000, ['primaryTitle'])

#Test Case 15
# Mystery_Function("Individual", 2000, ['startYear','runtimeMinutes' ,'primaryTitle'])
