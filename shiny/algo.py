#import sys
def range_csv(file):
    l=[]
    l_res=[]
    with open(file,"r") as f_csv:
        rd=f_csv.readlines()
        for i in rd[1:]:
            d={}
            sp=i.strip().split(",")
            d["mpg"]=float(sp[1])
            d["cyl"]=float(sp[2])
            l.append(d)
        
        for ii in l:
            a=ii["mpg"]/ii["cyl"]
            l_res.append(a)
        
        return l_res
            
            
#print(range_csv(sys.argv[1]))
