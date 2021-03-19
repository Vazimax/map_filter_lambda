import statistics

data = [98,100,95,99,95,93,100,97]
average = statistics.mean(data)
print(average)

output = list(filter(lambda x : x > average,data)) 
print(output)

countries = ['Morocco','Algeria','USA','China','Japan','Sweden']
output2 = list(filter(None,countries))
print(output2)