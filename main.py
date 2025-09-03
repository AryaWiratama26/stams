import stams

angka = [1,2,3,4,5]
shap = [2,3,7,5,4,5,4,5]

shap.sort()

print(shap)

print(stams.mean(angka))
print(stams.variance(angka, def_var='p'))
print(stams.std(angka))
print(stams.ranges(angka))
print(stams.median(shap))