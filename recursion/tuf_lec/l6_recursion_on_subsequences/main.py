

#https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6

def printAllSubsequences(index,list1,data):
    if index >= n:
        print(data)
        return 

    # printAllSubsequences()
    data.append(list1[index])
    printAllSubsequences(index+1,list1,data)
    data.pop()

    printAllSubsequences(index+1,list1,data)





if __name__ == "__main__":
    global n
    list1 = [1,3,5]
    n = len(list1)

    printAllSubsequences(0,list1,[])