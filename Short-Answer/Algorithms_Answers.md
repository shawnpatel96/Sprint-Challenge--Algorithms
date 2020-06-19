#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) time complexity because of the while loop. the while loop will iterate through each input and performs one operation per value. 


b) O(nlog n) because the for loop will iterate over each element but the inner loop is incrementing by twice its prev value which means it will take O(n) to finish.


c) O(n) time complexity, both returns are O(n). Each item of input is iterated through with recursion. 

## Exercise II
    Find highest point to drop an egg before it breaks?


    Split the floors using binary search. 
    We start in the middle of the building, if egg breaks,  we eliminate the upper half of floors since we know if an egg drops from those floors it will break as well. Than we can take the bottom half of the building and drop another egg, if it breaks eliminate the upper bottom half of the building. If it doesn't break. eliminate the bottom bottom half of the building, move upwards rinse and repeat.
    the run time would be O(logn) since we halves the floors every time we loop through.