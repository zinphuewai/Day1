# def greet():
#     print("Hello From UCSY")

# greet()

# def greet(name):
#     print(f"Hello, {name}!")

# greet('Ma Ma')

# def calculate_average(scores):
#     if len(scores) == 0:
#         return 0
#     return sum(scores)/len(scores)

# scores = [45,70,85]
# result = calculate_average(scores);
# print(result)
scores = [20,30,40,50,60]
def calculate_total(scores):
    return sum(scores)
result = calculate_total(scores)
print(result)

def calulate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)
average = calulate_average(scores)
print(average)

def classify_score(scores):
   if scores < 0 or scores >100:
      return "Invalid"
   elif scores >= 80:
      return "Excellent"
   elif scores >= 60:
      return "Good"
   elif scores >= 40:
      return "Pass"
   else:
      return "Fail"
print(classify_score(55))
print(classify_score(67))
print(classify_score(80))
print(classify_score(29))


def count_passed(scores):
   pass_count = 0
   for score in scores:
      if (score >= 40):
         pass_count +=1
      return pass_count
count= count_passed(scores)
print(count)
