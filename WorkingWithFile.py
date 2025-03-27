def summa_polozh_elementov(A): 
    n = len(A)     
    sum_polozhit = 0
    kolvo_polozhit = 0   
    
    for i in range(n):    
        for j in range(i + 1, n):     
            if A[i][j] > 0:              
                sum_polozhit += A[i][j]      
                kolvo_polozhit += 1         
                
    return sum_polozhit, kolvo_polozhit     



vvod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vvod.txt")
vivod = open("C:\\Users\\роман\\Desktop\\git\\Potapov\\пр10\\PotapovRomanMihailovich_UB32_vivod.txt", 'w')

matritsa = []
for i in vvod:
        spisok = [int(x) for x in i.split()]
        matritsa.append(spisok)

vivod.write(str(summa_polozh_elementov(matritsa)))

