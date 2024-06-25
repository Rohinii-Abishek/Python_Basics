# we use ''.join(result) to convert the list of characters back into a string.
def remove_duplicates(s):
    seen=set()
    result=[]
    duplicates=[]
    for char in s:
        if char not in seen:
          seen.add(char)
          result.append(char)
        else:
          duplicates.append(char)    
    return ''.join(result),duplicates

user_input=input("Enter the input:")
result,duplicates=remove_duplicates(user_input)
if remove_duplicates(user_input):
    print(f"The duplicate is/are {', '.join(set(duplicates))}")   
else:
    print(f"No duplicates found")    