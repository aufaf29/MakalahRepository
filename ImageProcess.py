from PIL import Image
import numpy
import time
import boyermoore
import knuthmorrispratt
import regexpress
import bruteforce

def regexPreprocess():
	for i in range(len(ar1)):
		res1[i] = res1[i].join([chr(item) for item in ar1[i]])
	for i in range(len(ar2)):
		res2[i] = res2[i].join([chr(item) for item in ar2[i]])

image1 = Image.open(r"TestPlan.png")
ar1 = numpy.array(image1)
ar1 = ar1.reshape(len(ar1), -1)

image2 = Image.open(r"SmallSub.png")
ar2 = numpy.array(image2)
ar2 = ar2.reshape(len(ar2), -1)

print("$ Algoritma Pattern Matching : \n")

print("$ 1. BruteForce")
start_time = time.time()
print(bruteforce.check(ar2,ar1))
print("time : " + str(time.time()*1000 - start_time*1000) + " ms")

print("$ 2. Knuth Morris Pratt")
start_time = time.time()
print(knuthmorrispratt.check(ar2,ar1))
print("time : " + str(time.time()*1000 - start_time*1000) + " ms")

print("$ 3. Boyer Moore")
start_time = time.time()
print(boyermoore.check(ar2,ar1))
print("time : " + str(time.time()*1000 - start_time*1000) + " ms")



# print("$ 4. Regular Expression")

# res1 = [""]*len(ar1)
# res2 = [""]*len(ar2)
# regexPreprocess()
# start_time = time.time()
# print(regexpress.check(res2,res1))
# print("time : " + str(time.time()*1000 - start_time*1000) + " ms")