# LeetCode 
# Combine Two Tables https://leetcode.com/submissions/detail/38460719/
# 
SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address ON Person.PersonId = Address.PersonId