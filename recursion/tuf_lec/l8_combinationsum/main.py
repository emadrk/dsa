
# https://www.youtube.com/watch?v=OyZFFqQtu98&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=8
# leetcode: https://leetcode.com/problems/combination-sum/description/
def printCombinationSum(index,arr,targetSum,data,finalRes):

    if index>=n:
        # tempd=0
        # for d in data:
        #     tempd+= d
        if targetSum ==0:
            temp = [d for d in data]
            finalRes.append(temp)

        return

    if arr[index]<=targetSum:
        data.append(arr[index])
        printCombinationSum(index,arr,targetSum-arr[index],data,finalRes)
        data.pop()

    printCombinationSum(index+1,arr,targetSum,data,finalRes)








if __name__ == "__main__":
    global n
    
    arr = [2,3,6,7]
    n = len(arr)
    targetSum = 7
    finalRes = []
    printCombinationSum(0,arr,targetSum,[],finalRes)
    print(finalRes)