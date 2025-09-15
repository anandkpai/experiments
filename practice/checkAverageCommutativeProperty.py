from statistics import mean

test_data  = [1,1,2,3,4]

print(mean(test_data))

t1 = mean(test_data[:3:])
t2 = mean(test_data[3::])

print(t1,t2, mean([t1,t2]))

