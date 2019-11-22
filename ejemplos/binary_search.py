import random


def binary_search(data,target,low,high):
    if low > high:
        return False
    
    mid=(low+high)//2

    if target ==data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target,low,mid-1)
    elif target > data[mid]:
        return binary_search(data, target,mid+1,high)





if __name__ == "__main__":
    data =[random.randint(0,100) for i in range(100)]#comprehension
    sorted_data= sorted(data)
    print(sorted_data)
    target=int(input('Cual es el numero que deseas busacr?'))
    found = binary_search(data,target,0,len(data)-1)
    print(found)
