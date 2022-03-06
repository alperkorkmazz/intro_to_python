import statistics
data=[i**2 for i in range(10)]
avg=statistics.mean(data)
print(data)
print(avg)
gfiltered=filter(lambda x: x>avg, data)
print(list(gfiltered))
lfiltered=filter(lambda x: x<avg, data)
print(list(lfiltered))
#filter(None,list) -> None values are "",0,0.0,0j,[],(),{}, False, None
countries=["","China","","", "Ecuador", "Greece","Iran"," ","0",0]
print(list(filter(None,countries)))

