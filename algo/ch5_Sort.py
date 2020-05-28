# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:28:56 2020

@author: yyuan
"""

"""
排序(Sort)
BubbleSort    O(n)~O(n^2) Stable
SelectionSort O(n^2)      Not Stable 
InsertionSort O(n)~O(n^2) Stable
ShellSort     random(step)~O(n^2) Not Stable
QuickSort     O(nlogn)~O(n^2) Not stable  middle value~reverse value
MergeSort     O(nlogn)    Stable
"""

def BubbleSort(list):
    for i in range(len(list) - 1):# number of iterations
        count = 0 #Counter to see if exchangement has finished and iteration could stop
        for j in range(len(list)-1-i): # Judge and exchange from beginning
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                count+=1
        if count ==0:
            return
        print(list)

def SelectionSort(list):
    n = len(list)
    for i in range(n-1):#Selection Area
        min_index = i
        for j in range(i+1,n):# Find the index of minimum
            if list[j]<list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
        print(list)

def InsertionSort(list):
    n = len(list)
    for i in range(1,n):#The element to insert from unsorted part
        for j in range(i,0,-1):# Compare the element with previous sorted sequence
            if list[j] < list[j-1]:
                list[j-1],list[j]= list[j],list[j-1]
            else:
                break
        print(list)
        
def ShellSort(list):
    n = len(list)
    gap = n//2
    while gap>0:
        for start in range(gap,n): #Start from gap
            for i in range(start,gap-1,-gap):#exchange
                if list[i] < list[i-gap]:# Core of insertion sort
                    list[i-gap],list[i] = list[i],list[i-gap]
                    print(list)
                else:
                    break
        gap=gap//2
            
def QuickSort(list,start,end):
    #递归退出条件
    if start >= end:
        return
    pivot = list[start]
    low = start
    high = end
    #当low与high没有相等时
    while low < high:
        #当low<high,从high开始移动，if high>pivot,移动high label，否则与low交换
        while low<high and list[high] >= pivot:
            high -=1
        list[low]= list[high] 
        print(list)
        #结束high label移动，判断low label是否可以移动
        #上述循环结束，说明找到一个小于pivot的数，并与low label交换，移动至左边
        while low<high and list[low] < pivot:
            low+=1
        #low label 结束移动，发现一个大于pivot的数，与high label交换，移动至右边
        list[high] = list[low]
        print(list)
    #找到pivot
    list[low] = pivot
    
    #递归
    QuickSort(list,start,low-1)
    QuickSort(list, high+1, end)
  
def MergeSort(list):
    n = len(list)
    if n <= 1:
        return list
    
    #Split 拆分
    mid = n//2
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    # print(left)
    # print(right)
    
    #合并
    return merge(left,right)

def merge(left,right):
    result = []
    left_cursor =0
    right_cursor = 0
    #比较左右大小
    while left_cursor < len(left) and right_cursor <len(right):
        if left[left_cursor] <= right[right_cursor]:
            result.append(left[left_cursor])
            left_cursor +=1
        else:
            result.append(right[right_cursor])
            right_cursor +=1
    #指针走完后，剩下的数加入列表
    result += left[left_cursor:]
    result += right[right_cursor:]
    # print(result)
    return result


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    #BubbleSort(li)
    #SelectionSort(li)
    #InsertionSort(li)
    #ShellSort(li)
    #QuickSort(li, 0, 8)
    
    #li = MergeSort(li)
    #print(li)
        
    
