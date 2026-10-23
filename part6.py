# for i in range(5):
#     print(i);

# scores =[20,70,40,30,10]
# for score in scores:
#     print(score);

# count = 1;
# while count<=5:
#     print(count)
#     count+=1

scores = [45, 70, 85, 30, 90, 55]
pass_count = 0
fail_count = 0
total = 0
for score in scores:
 total += score
average = total / len(scores)
print("Total:", total)
print("Average:", average)
for score in scores:
    if score <=40:
       fail_count +=1
    else:
       pass_count +=1
    
print(fail_count);
print(pass_count);