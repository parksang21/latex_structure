with open('lg_file_list.txt.m', 'r') as f:
    lines = f.readlines()
    val = []
    total=0
    for l in lines:
        total+=1
        lt = l.strip()[-1]
        if lt == 'g':
            #print(l)
            continue
        #print(int(lt))
        val.append(int(lt))
print("Total Number of Validation Set(except span): ",total/2)
print("AP: %.4f"%(sum(val)/(total/2)))

