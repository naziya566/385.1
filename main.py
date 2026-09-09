print('Hello World')
# dataset
# square brakets represent a list
# list, indexed (ordered), list of values
data = [1, 5, 6, 6, 8, 13, 14, 18]
print('Given Data:', data)

length = len(data)
print('Length:', length)

# 1. Calculate the mean sum(all values) / length
def findAvg(list):
    sum = 0

    for val in list:
        sum = sum + val

    return sum / length

avg = findAvg(data)

print('Avg:', avg)

# 2. Calculate Squared differences
#   # Find the difference
#   # Square the difference
sqr_diff = []

for val in data:
     output_val = (val - avg)**2
     sqr_diff.append(output_val)

print('Squared Differences:', sqr_diff)

# 3. Average of squared differences (Variance)
variance = findAvg(sqr_diff)
print('Variance:', variance)

# 4. Take the sqaure root of the variance = StDev
standard_dev = variance**0.5

print('Standard Deviation:', standard_dev)