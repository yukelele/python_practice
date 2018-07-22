def printMaxActivities(arr, n):
    arr.sort(key=lambda arr: arr[1])
    i = 0
    print(arr[i][0],arr[i][1])
    for j in range(1,n):
        if arr[j][0] >= arr[i][1]:
            print(arr[j][0],arr[j][1])
            i = j


if __name__ == "__main__":
    arr = [[5,9],[1,2],[3,4],[0,6],[5,7],[8,9]]
    printMaxActivities(arr,len(arr))

