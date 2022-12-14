
# https://www.youtube.com/watch?v=eQCS_v3bw0Q&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=7

def printSubsequenceOfSumK(index,arr,targetSum,variableSum,data):

    if index>=n:
        if variableSum== targetSum:
            print(data)

        return


    data.append(arr[index])
    variableSum +=arr[index]
    printSubsequenceOfSumK(index+1,arr,targetSum,variableSum,data)
    data.pop()
    variableSum -=arr[index]
    printSubsequenceOfSumK(index+1,arr,targetSum,variableSum,data)





if __name__ == "__main__":
    global n
    
    arr = [1,2,1,4,5,6,7,8,7,6]
    n = len(arr)
    targetSum = 12
    variableSum = 0
    printSubsequenceOfSumK(0,arr,targetSum,variableSum,[])
