print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh? (numeric only)", end=' ')
weight = int(input())

print("What's your target weight (numeric only)?", end=' ')
target_weight = int(input())
weight_goal = weight - target_weight

# there would normally be a ton of input and condition checking here

print(f"So, you're {age} old, {height} tall and {weight} pounds heavy.")
# note: need f"" construction on each part of the string
print(f"If you want to get to a weight of {target_weight}, " +
    f"you will need to lose {weight_goal} pounds.")
