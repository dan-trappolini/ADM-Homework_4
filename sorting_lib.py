#!/usr/bin/env python
# coding: utf-8

# # 2. Alphabetical Sort

# ## 1. Build your own implementation of Counting Sort. If it's based (based, not copied!) on some reference on Internet, please cite it.

# We learnt about Counting Sort in this video: https://www.youtube.com/watch?v=TTnvXY82dtM. 
# <br><br>
# As the input, we have the unsorted list of numbers. We create a list (let's call it "counter") of length between maximum value and minimum value in the input list.  We put the number of occurences of each number of the input list in the new list at the corresponding position. 
# <br><br>
# Then, we create another list. Let's call it "sum counter". Its first cell is the same as in "counter" list. The next ones sums all the previous cells and the corresponding cell in the "counter". 
# <br><br>
# The last step is to create the final list of the same length as the input list. We look at the first number in the input array. It is now our index. We look at the corresponding position in the "sum counter" and put its value in the final array. We reduce the value of "sum_counter" by one. Then we repeat it for all the numbers in the input array.

# In[342]:


def Counting_Sort(a):
    counter_range=max(a)-min(a)+1 #O(1)
    counter=[0]*counter_range #O(1)

    for i in a: #O(n)
        counter[i-min(a)]+=1 #O(1)

    sum_counter=counter #O(1)
    for j in range(1,counter_range): #O(m)
        sum_counter[j]=sum_counter[j-1]+counter[j] #O(1)

    final=[0]*len(a) #O(1)

    for k in a: #O(n)
        final[sum_counter[k-min(a)]-1]=k #O(1)
        sum_counter[k-min(a)]-=1 #O(1)

    return final


# Information for the next task - this algorithm works in linear time O(n+m). We cannot say which value is bigger. We use n as the length of the input array and m as the length of counter (and counter_sum).

# ## 2. Build an algorithm, based on your implementation of Counting Sort, that receives in input a list with all the letters of the alphabet (not in alphabetical order), and returns the list ordered according to alphabetical order. Discuss time complexity (theoretically and empirically).

# As was said on Slack, we consider only lowercase letters. The algorithm is the same as in the previous exercise. The only thing we have to do is converting letters to numbers - we do it through ASCII table. We put in comments the running time of each step using big O notation. It should run in linear time bacause none "for" loop has another loop inside.

# In[368]:


def Alphabetical_Order(b):
    import string
    a=[] #O(1)

    for index in range(len(b)): #O(n)
        a.append(ord(b[index])) #O(1)
    
    a=Counting_Sort(a) #O(n) - in this case lengths of input list and the counter are the same because we take as input a list of ALL letters of the alphabet
    
    answer=[] #O(1)
    for i in a: #O(n)
        answer.append(chr(i)) #O(1)

    return answer #O(1)


# The algorithm runs in linear time - O(n+n+constants) which we can simplify to O(n).

# ## 3. Build an algorithm, based on your implementation of Counting Sort, that receives in input a list of length m, that contains words with maximum length equal to n, and returns the list ordered according to alphabetical order. Discuss time complexity (theoretically and empirically).

# As was said on Slack, we consider only lowercase letters.<br>
# We got the idea of Radix sort from https://pastebin.com/tTD7QSsb.

# In[371]:


import string

def Alphabetical_Order_Words(b):
    m=len(b)
    n=max(len(w) for w in b) #O(m)
    #We set equal lengths of each string by adding "|" at the end of shorter words
    new_b=[] 
    for word in b: #O(m)
        new_arr = ['|' * (n - len(word))]
        new_b.append(word+''.join(new_arr))


    letters=[]
    dic={}

    
    for indexx in range(n-1,-1,-1): #O(n)
        #We convert characters to numbers using ASCII table
        a=[[] for _ in range(m)]

        for index in range(m): #O(m)
            for index_2 in range(n): #O(n)
                x=list(new_b[index])
                a[index].append(ord(x[index_2]))


                
        #We create lists of letters, starting from the last letter of each word
        for i in range(m): #O(m)
            letters.append(a[i][indexx])


         
        #We create dictionary whose keys are words and values are following letters, from the last to the first one
        dic={}
        
        for i in range(m): #O(m)
            dic[new_b[i]]=letters[i]


        letters=Counting_Sort(letters) #We sort letters alphabetically

        #We create a dictionary to store words sorted by following characters
        final={}
        for i in range(m): #O(m)
            for word in new_b: #O(m)
                if dic[word]==letters[i]: #O(1)
                    final[word]=letters[i]
        letters=[]
        dic=final #We keep previously sorted dictionary for next iterations

        sorted_list=[] #We  create list of sorted words
        for i in dic: #O(m)
            sorted_list.append(i)

        new_b=[] #We store sorted words in a list
        for i in dic: #O(m)
            new_b.append(i)


    return ([i.replace('|', '') for i in sorted_list]) #O(m)


# We put running time of each step in the comments. We did not take into account the constant time because it is not significant if we already have O(n). The running time of the whole algorithm is O(m+m+m+n*((m+n)+m+m+(m+m)+m+m) which we can simplify to O(n^2+m*n).
