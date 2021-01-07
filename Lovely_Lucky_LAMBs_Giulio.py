def solution(total_lambs):
    generous=[]
    stingy=[]
    if total_lambs == 0:
        pass
    elif total_lambs == 1:
        generous.append(1)
        stingy.append(1)
    elif total_lambs == 2:
        generous.append(1)
        stingy.append(1)
        generous.append(1)
        stingy.append(1)
    elif total_lambs == 3:
        generous.append(1)
        stingy.append(1)
        generous.append(2)
        stingy.append(1)
        print(generous,'\n',stingy)
    else:
        generous.append(1)

        while total_lambs-sum(generous) >= generous[-1]*2:
            generous.append(generous[-1]*2)
            print(generous)

        print('-----------------------------------------')

        stingy.append(1)
        stingy.append(1)

        while (total_lambs-sum(stingy)) >= (stingy[-1]+stingy[-2]):
            stingy.append(stingy[-1]+ stingy[-2])
            print(stingy)
        
    return print(len(stingy)-len(generous))

solution(10**12)