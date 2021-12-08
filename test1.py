def array_sum(arr):
    if len(arr) == 1:
        return arr[0]

    median = int(len(arr)/2)

    return array_sum(arr[0:median]) + array_sum(arr[median:len(arr)])


lst = [1,2,3,4,5,6,7]
fff = array_sum(lst)
print(fff)