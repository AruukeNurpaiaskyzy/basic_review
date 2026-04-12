# fruits = ['apple', 'banana', 'cherry']
# print('banana' in fruits)
# # print(fruits)


# print(len(fruits))


# my_lists = [1,2,3]
# my_lists2 = [2,3,4]
# print(my_lists==my_lists2)


DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up (*, current_experience: int, gained_experience: int) -> bool:
 total_experience = current_experience+gained_experience
 level_up = False
 if total_experience>=DEFAULT_LEVEL_EXPERIENCE:
    level_up = True
    return level_up

result = is_leveled_up(current_experience=150, gained_experience=60)
print(result)  




# DEFAULT_LEVEL_EXPERIENCE = 200

# def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
#     total_experience = current_experience + gained_experience
#     return total_experience >= DEFAULT_LEVEL_EXPERIENCE










