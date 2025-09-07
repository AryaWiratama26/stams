import stams

number = [1,2,3,4,5]
str_list = ["a","b","c","d","a"]

print(stams.mean(number))
print(stams.variance(number, def_var='p'))
print(stams.std(number))
print(stams.ranges(number))
print(stams.median(number))
print(stams.modus(str_list))