import csv
import time
import json
import pandas as pd

"""
Note : For test cases 7-10, you need to extract the required data (filter on conditions mentioned above)
and rename it to appropriate name as mentioned in the test case descriptions. You need to write the code
to perform this extraction and renaming, at the start of the skeleton file.
"""

column_names= ['tconst', 'primaryTitle', 'originalTitle', 'startYear',
               'runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'ordering',
               'category', 'job', 'seasonNumber', 'episodeNumber', 'primaryName', 'birthYear',
               'deathYear', 'primaryProfession']


#############################################################################################################
# Data Filtering
#############################################################################################################
def data_filtering(filelocation, num):
    """
    Data Filtering is for the test cases from 7 to 10.
    filelocation: imdb_dataset.csv location
    num: if num == 1 -> filter data based on years (years in range 1941 to 1955)
         if num == 2 -> filter data based on genres (genres are either ‘Adventure’ or ‘Drama’)
         if num == 3 -> filter data based on primaryProfession (if primaryProfession column contains substrings
                        {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
         if num == 4 -> filter data based on primary Names which start with vowel character.

    """
    df = pd.read_csv(filelocation)# Load the imdb_dataset.csv dataset
    if(num==1):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on years (years in range 1941 to 1955)
        df_year = df[(df['startYear'].astype(int)>=1941) & (df['startYear'].astype(int)<=1955)]
        #Store your filtered dataframe here
        df_year.reset_index(drop=True).to_csv("imdb_years_df.csv", index=False)

    if(num==2):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on genres (genres are either ‘Adventure’ or ‘Drama’)
        df_genres = df[(df['genres'] ==('Adventure')) | (df['genres']==('Drama'))]
        #Store your filtered dataframe here
        df_genres.reset_index(drop=True).to_csv("imdb_genres_df.csv", index=False)
    if(num==3):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primaryProfession (if primaryProfession column contains
        #substrings {‘assistant_director’, ‘casting_director’, ‘art_director’, ‘cinematographer’} )
        prof = ['assistant_director', 'casting_director', 'art_director', 'cinematographer']
        df_professions =df[df['primaryProfession'].apply(lambda x: any(i in x for i in prof))] #Store your filtered dataframe here
        df_professions.reset_index(drop=True).to_csv("imdb_professions_df.csv", index=False)
    if(num==4):
        #NEED TO CODE
        #Implement your logic here for Filtering data based on primary Names which start with vowel character.
        vowels = ['A', 'E', 'I', 'O', 'U']
        df_vowels = df[df['primaryName'].str[0].apply(lambda x: x.upper() in vowels)] #Store your filtered dataframe here
        df_vowels.reset_index(drop=True).to_csv("imdb_vowel_names_df.csv", index=False)


#############################################################################################################
#Quick Sort
#############################################################################################################

def quicksort(arr, columns):
    if len(arr) <= 1:
        return arr
    else:
        pivot_Element = arr[len(arr) // 2]
        left_Sorted_array = []
        middle_Sorted_array = []
        right_sorted_array = []
        
        for imdb_index in arr:
            Return_comparison = compare(imdb_index, pivot_Element, columns)
            if Return_comparison < 0:
                left_Sorted_array.append(imdb_index)
            elif Return_comparison == 0:
                middle_Sorted_array.append(imdb_index)
            else:
                right_sorted_array.append(imdb_index)

        return quicksort(left_Sorted_array, columns) + middle_Sorted_array + quicksort(right_sorted_array, columns)

    #NEED TO CODE
    #Implement Quick Sort Algorithm
    #return Sorted array
    
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Selection Sort
#############################################################################################################
def selection_sort(arr, columns):
  
    for imdb_row in range(len(arr)):
        min_index = imdb_row
        for imdb_unsortedlist in range(imdb_row+1,len(arr)):
            for imdb_par in range(1,len(columns)):
                if arr[imdb_unsortedlist][imdb_par] < arr[min_index][imdb_par]:
                    min_index = imdb_unsortedlist
                    break
                elif arr[imdb_unsortedlist][imdb_par]> arr[min_index][imdb_par]:
                    break
            
        arr[imdb_row],arr[min_index]=arr[min_index],arr[imdb_row]

    return arr
  
#############################################################################################################
#Heap Sort
#############################################################################################################
def max_heapify(arr, n, i, columns):
    """
    arr: the input array that represents the binary heap
    n: The number of elements in the array
    i: i is the index of the node to be processed
    columns: The columns to be used for comparison

    The max_heapify function is used to maintain the max heap property
    in a binary heap. It takes as input a binary heap stored in an array,
    and an index i in the array, and ensures that the subtree rooted at
    index i is a max heap.
    """
    largest =i
    left_child =2*i +1
    right_child = 2*i+2
    
    if(left_child<n):
        if compare(arr[largest],arr[left_child],columns)<0:
            largest=left_child
        
    if (right_child<n):
        if compare(arr[largest],arr[right_child],columns)<0:
            largest=right_child
        
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,n,largest,columns)
        #print(arr)


def build_max_heap(arr, n, i, columns):
    """
    arr: The input array to be transformed into a max heap
    n: The number of elements in the array
    i: The current index in the array being processed
    columns: The columns to be used for comparison

    The build_max_heap function is used to construct a max heap
    from an input array.
    """
    
    #NEED TO CODE
    for imdb_index in range ((n//2)-1,-1,-1):
        max_heapify(arr,n,imdb_index,columns)
    #Implement heapify algorithm here

def heap_sort(arr, columns):
    """
    # arr: list of sublists which consists of records from the dataset in every sublists.
    # columns: store the column indices from the dataframe.
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Implement Heap Sort Algorithm
    #return Sorted array
    n=len(arr)
    i=n//2-1
    build_max_heap(arr, n, i, columns)
    for imdb_index in range(n-1,0,-1):
        
        arr[imdb_index],arr[0] =arr[0],arr[imdb_index]
        #print(arr,x,columns)
        max_heapify(arr,imdb_index,0,columns)
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Shell Sort
#############################################################################################################
def compare(row1,row2,columns):
    for col in range(1,len(columns)):
        if(row1[col]<row2[col]):
            return -1
        elif(row1[col]>row2[col]):
            return 1
        elif((row1[col]==row2[col])):
            continue
    return 0


def shell_sort(arr, columns):
    """
    arr: a list of lists representing the 2D array to be sorted
    columns: a list of integers representing the columns to sort the 2D array on
    Finally, returns the final sorted 2D array.
    """
    #NEED TO CODE
    #Implement Shell Sort Algorithm
    #return Sorted array
    len_array = len(arr)
    Intervel = len_array // 3
    
    while Intervel > 0:
        for unsorted_index in range(Intervel, len_array):
            temp = arr[unsorted_index]
            unsorted_after_gap = unsorted_index
            while unsorted_after_gap >= Intervel and compare(arr[unsorted_after_gap - Intervel],temp,columns)>0:
                arr[unsorted_after_gap] = arr[unsorted_after_gap - Intervel]
                unsorted_after_gap -= Intervel
    
            arr[unsorted_after_gap] = temp
    
        Intervel //= 3
    return arr

#############################################################################################################
#Merge Sort
#############################################################################################################
def merge(left_sublist, right_sublist, columns):
    """
    left: a list of lists representing the left sub-array to be merged
    right: a list of lists representing the right sub-array to be merged
    columns: a list of integers representing the columns to sort the 2D array on

    Finally, after one of the sub-arrays is fully merged, the function extends the result
    with the remaining elements of the other sub-array and returns the result as the final
    sorted 2D array.
    """
    #NEED TO CODE
    sorted_result = []
    left_merge_pointer, right_merge_pointer = 0, 0
    while left_merge_pointer < len(left_sublist) and right_merge_pointer < len(right_sublist):
        
        #for col in range(1,len(columns)):
        if compare(right_sublist[right_merge_pointer],left_sublist[left_merge_pointer],columns)>=0:
            sorted_result.append(left_sublist[left_merge_pointer])
            left_merge_pointer += 1
        else:
            sorted_result.append(right_sublist[right_merge_pointer])
            right_merge_pointer+= 1
    
    sorted_result += right_sublist[right_merge_pointer:]
    sorted_result += left_sublist[left_merge_pointer:]
    return sorted_result

def merge_sort(data, columns):

    if len(data) <= 1:
        return data
    mid_array = len(data) // 2
    left_sublist = data[:mid_array]
    right_sublist = data[mid_array:]
    left_sublist = merge_sort(left_sublist, columns)
    right_sublist = merge_sort(right_sublist, columns)
    #Need to Code
    #Implement Merge Sort Algorithm
    #return Sorted array
    return merge(left_sublist, right_sublist, columns)
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
#Insertion Sort
#############################################################################################################
def insertion_sort(arr, columns):
   
    for imdb_sortedlist in range(1,len(arr)):
        index = imdb_sortedlist
        temp = arr[imdb_sortedlist]
        imdb_unsorted=imdb_sortedlist-1
        while(imdb_unsorted>=0) and compare(arr[imdb_unsorted],temp,columns)>0:
          
            index = imdb_unsorted
            arr[imdb_unsorted+1]=arr[imdb_unsorted]
                
           # elif(arr[imdb_unsorted][col_index] < temp[col_index]):
                
            imdb_unsorted = imdb_unsorted-1
        arr[index]=temp
    return arr
    #Output Returning array should look like [['tconst','col1','col2'], ['tconst','col1','col2'], ['tconst','col1','col2'],.....]
    #column values in sublist must be according to the columns passed from the testcases.

#############################################################################################################
# Sorting Algorithms Function Calls
#############################################################################################################
def sorting_algorithms(file_path, columns, select):
    df= pd.read_csv(file_path).applymap(lambda x: x.strip() if isinstance(x, str) else x)#.apply(lambda y: y.str.strip() if y.dtype == "object" else y)
    #read imdb_dataset.csv data set using pandas library
    column_vals = [0]+ [df.columns.get_loc(column) for column in columns]
    data = df.iloc[:,column_vals].values.tolist()
   
#############################################################################################################
# Donot Modify Below Code
#############################################################################################################
    if(select==1):
        start_time = time.time()
        output_list = insertion_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==2):
        start_time = time.time()
        output_list = selection_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==3):
        start_time = time.time()
        output_list = quicksort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==4):
        start_time = time.time()
        output_list = heap_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==5):
        start_time = time.time()
        output_list = shell_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
    if(select==6):
        start_time = time.time()
        output_list = merge_sort(data, column_vals)
        end_time = time.time()
        time_in_seconds = end_time - start_time
        return [time_in_seconds, list(map(lambda x: x[0], output_list))]
