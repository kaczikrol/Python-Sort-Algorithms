#Przemyslaw Kaczmarek 2017/11/21

def InsertionSort(list):
    lenght = len(list)
    for i in range(1,lenght):
        valueToInsert=list[i]
        insertPosition=i
        while insertPosition>0 and list[insertPosition-1]>valueToInsert:
            list[insertPosition]=list[insertPosition-1]
            insertPosition-=1
        list[insertPosition]=valueToInsert
    print(list)


def main():
    list=[]
    lenght=eval(input("Insert length of list: "))
    for i in range(lenght):
        value=eval(input("Insert value to list: "))
        list.append(value)
    print(InsertionSort(list))
main()