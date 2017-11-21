#Przemyslaw Kaczmarek 2017/11/21

def SelectionSort(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        if min!=i:
            minValue=list[min]
            list[min]=list[i]
            list[i]=minValue
    return list

def main():
    list=[]
    length=eval(input("Insert lenght of list: "))
    for i in range(length):
        value=eval(input("Insert value to list: "))
        list.append(value)
    print(SelectionSort(list))

main()