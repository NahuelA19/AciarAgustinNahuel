def bubble_sort(list):

 n = len(list)
 for i in range(n):
       
        for j in range(0, n-i-1):
            
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]