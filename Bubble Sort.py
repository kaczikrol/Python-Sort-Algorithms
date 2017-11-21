#Przemyslaw Kaczmarek 2017/11/21

def BubbleSort(list):
    length=len(list)
    for i in range(length-1):
        changes = False
        for j in range(length-1):
            firstValue=list[j]
            secondValue=list[j+1]
            if firstValue>secondValue:
                list[j]=secondValue
                list[j+1]=firstValue
                changes=True
        if changes==False:
            break
    return list

def main():
    list=[]
    length=eval(input("Insert length of list: "))
    while length>0:
        inputValue=eval(input("Insert value into list: "))
        list.append(inputValue)
        length-=1
    print(BubbleSort(list))
main()