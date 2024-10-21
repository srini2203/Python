def count_substring_occurrences(main_str, sub_str):
    count = 0
    for i in range(len(main_str) - len(sub_str) + 1):
        if main_str[i:i + len(sub_str)] == sub_str:
            count += 1
    return count


main_str = input("Enter the string: ")
sub_str = input("Enter the substring: ")


occurrences = count_substring_occurrences(main_str, sub_str)

print("The number of times the substring occurs in the string is:", occurrences)
