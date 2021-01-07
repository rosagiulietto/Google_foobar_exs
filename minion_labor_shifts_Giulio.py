def solution(data,n):
    print('INPUT: ',data)
    if n==0:
        del data[:]
        return print('OUTPUT: ',data)
    elif n!=0:
        data_2=[]
        for number in data:
            data_2.append(data.count(number))
        dict={}
        for number in range(0,len(data),1):
            dict[data[number]]=data_2[number]
        del data[:]
        for key, value in dict.items():
            if value<=n:
                data.append(key) 
            else:
                continue
        return print('OUTPUT: ',data)

user_data=[1,2,2,3,3,3,4,5,5]
n=(1)
solution(user_data, n)