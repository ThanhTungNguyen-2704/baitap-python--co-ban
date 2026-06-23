students = ["Tung","Ly","Dung","Hieu","Minh"] 
print(students[0])
print(students[-1])

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0:3])
print(numbers[8:])
for i in range (len(numbers)) :
	if i % 2 ==0 :
		print(numbers[i])

print(numbers.reverse())

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range (len(matrix)):
	for j in range (len(matrix[i])):
		if matrix[i][j] == 6:
			print (matrix[i][j])

tasks = []
tasks.append("hoc Python")
tasks.append("hoc toi uu hoa")
tasks.append("hoc DSA")
tasks.append("Hoc sql")
tasks.append("Hoc tieng anh")
revenue = [100, 200, 300]
revenue.insert(1,150)

list_a = [1,2,3]
list_b = [4,5,6]

list_a.extend(list_b)
cart = ["áo", "quần", "giày", "mũ", "áo"]
cart.remove("áo") #con ao 
last_item = cart.pop()
cart.pop(0)

#remove xoa gia tri cua phan tu ( neu co nhieu gia tri trung nhau thi xoa cai dau tien) ( xoa gia tri)
#pop(i) lay ra phan tu thu i va xoa no (xoa vi tri, tra ve phan tu da xoa)
#del list[i] chi xoa phan tu i ( xoa vi tri)

data = [1, 2, 3, 4, 5]
data.clear()
print(len(data))

temperatures = [22, 25, 19, 30, 25, 28, 25]
for i in range (len(temperatures)):
	if temperatures[i] == 25 :
		print(i)
		break
count = int(0) 
for i in range (len(temperatures)):
	if temperatures[i] == 25 :
		count += 1
print(count)
for x in temperatures :
	if x == 35 :
		print("Có")
	else :
		print ("Không")

scores = [88, 45, 76, 90, 12, 67]
scores.sort()
result3 = scores.sort(reverse = True)

list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)
#Du doan list 2 chi den dia chi cua list 1 vi vay khi list 2 append(4) thi list 1 cung append(4) vi vay ket qua la [1,2,3,4]
#Sua lai Cach 1
list3 = list1.copy()
#Sua lai cach 2
list4 = list1[:]

nested = [[1,2], [3,4]]

nested2 = nested.copy()
nested2[0][0] = 999
print(nested[0][0])
 #nest[0][0] khong bi anh huong vi nested2 la  ban sao doc lap voi nested 


daily_usage = [1.2, 0.8, 3.5, 2.1, 0.0, 4.2, 1.9]

sum = float(0)
for x in daily_usage:
 	sum += x
print(sum)
max = float(-9999)
indexMax = int(-1)
min = float(9999)
indexMin = int(-1)

for i in range  (len(daily_usage)) :
	if (daily_usage[i] > max):
		max = daily_usage[i]
		indexMax =i ;

	elif (daily_usage[i] < min):
		min = daily_usage[i]
		indexMin = i 
count2 = int(0)
for x in daily_usage:
	if x > 2 :
		count2 += 1

print(count2)

print(round(sum / len(daily_usage),2))




