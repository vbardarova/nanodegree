# Problem 4

The algorithm here is recursion. We check whether the name of the group is tha same as the user, next we check what's the users list of that group. Next, we proceed at the child groups. Depending on whether we find any users, we return True or False

    
```
Time Complexity: O(#of groups in a group * #of users in each of those groups)
Space Complexity: O(#of groups in a group * #of users in each of those groups)
```


