# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:36:38 2018

@author: Gebruiker
"""

"""
#Question
#Given two strings, return True if either of the strings appears at the very 
#end of the other string, ignoring upper/lower case differences (in other words,
# the computation should not be "case sensitive"). Note: s.lower() returns the 
#lowercase version of a string.
#
#
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True"""
#
#
#"""solved where each function only does one thing""""
#def end_other(a, b):  
#  lower_case_first_word, lower_case_second_word = make_words_lowercase(a, b)
#  first_word_length, second_word_length = get_length_ofwords(lower_case_first_word, lower_case_second_word)
#  word_in_word = is_either_word_in_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length)
#  if word_in_word==False:
#      return False
#  else:
#      return is_word_at_end_of_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length)
#
#def make_words_lowercase(a, b):
#  lower_case_first_word = a.lower()
#  lower_case_second_word = b.lower()
#  return (lower_case_first_word, lower_case_second_word)
#  
#def get_length_ofwords(lower_case_first_word, lower_case_second_word):
#  first_word_length = (len(lower_case_first_word))
#  second_word_length = (len(lower_case_second_word))
#  return (first_word_length, second_word_length)
#  
#def is_either_word_in_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length):
#  if (lower_case_second_word in lower_case_first_word) or (lower_case_first_word in lower_case_second_word):
#    return is_word_at_end_of_other(lower_case_first_word, lower_case_second_word,first_word_length, second_word_length)
#  else:
#    return False
#end_other('Hiabc', 'abc')
#end_other('Hiabcx', 'bc')
#
#"""or alternative method""""
#def end_other(a, b):
#  lower_case_first_word = a.lower()
#  first_word_length = (len(lower_case_first_word))
#  lower_case_second_word = b.lower()
#  second_word_length = (len(lower_case_second_word))
#  print(lower_case_first_word[-second_word_length::])
#  print(lower_case_second_word[-first_word_length::])
#  
#  
#  if (lower_case_second_word in lower_case_first_word) or (lower_case_first_word in lower_case_second_word):
#    if (lower_case_first_word[-second_word_length::]== lower_case_second_word[-first_word_length::]):
#        print(True)
#    else:
#        print(False)
#  else:
#    print(False)
#
#
#end_other('Hiabc', 'abc')
#end_other('Hiabcx', 'bc')

#def count_evens(nums):
#  count = 0
#  print(len(nums))
#  for n in range(len(nums)-1):
#    if nums[n]%2 == 0:
#      count = count + 1
#    else:
#      count = count
#  return count
#     
#print(count_evens([1, 3, 5]))

#def big_diff(nums):
#    nums.sort()
#    answer = nums[-1] - nums[0]
#    print(answer)
#    
#big_diff([10, 3, 5, 6])

#def sum13(nums):
#  sum = 0
#  for n in nums:
#     if n==13:
#         nums.remove(n)
#         print(nums)
#     else:
#         sum += n
#         print(sum)
#  return sum
#  
#print(sum13([1, 2, 13, 2, 3, 13, 1]))


def sum67(nums):
  

sum67([1, 2, 2, 6, 99, 99, 7])


