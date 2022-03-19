
# Election Analysis
## Project Overview

This repo takes a glimpse at a Colorado Board of Elections' recent local congressional election.The repo includes a look at the total # of votes, the total counts of candidates who received votes, their respective percentages of votes, a determination of winner based on the popular vote; and county vote measures, including, the number of votes per county, the percentage of votes per county, and the county with the greatest number of votes and percentage of the congressional race won. 

<img width="298" alt="Screen Shot 2021-09-19 at 8 01 55 PM" src="https://user-images.githubusercontent.com/89168119/133947545-762bd03a-9c5e-4d6d-a2c7-ed0f8614c557.png">

## Resources

1. election_results.csv 
2. Software: Python 3.6.1, Visual Studio Code 1.38.1

## Summary 

An analysis of the Colorado congressional election was taken. Looking at number of votes cast, candidates voted for and percentage of votes, and counties and subsequent winner of election based off the data given. There was a total of 369,711 votes. There were three candidates who recieved votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. With the candidates receiving, 23%, 73.8%, and 3.1%, respectively. Three counties participated in the election: Denver, Arapahoe, and Jefferson. And three counties accounting for 82.8%, 6.7% , and 10.5 %7%, respectively. Diana DeGette came out as the winner of the popular vote. 

## Results

- A total of 369,711 votes were cast in the election. 
- Votes by County
  - Jefferson: 38,855 (10.5%)
  - Denver: 306,055 (82.8%)
  - Arapahoe: 24,801 (6.7%)
- Denver County had the largest number of votes with 306,055 votes. 
- Votes by Candidate
  - Charles Casper Stockham 85,213 (23%)
  - Diana DeGette 272,892 (73.8%)
  - Raymon Anthony Doane 11,606 (3.1%)
- Diana DeGette won the election with 272,892 votes. 

## Election Audit Summary

This script offers great insight to other elections as any data source contained in a .csv can be used. The code could be used as is, or modified and extended to include filters such as percentages of votes per candidate in a county--to give users a more detailed look into how the voters are voting by county. To achieve this, a line of code that contains a conditional statement with the candidate's names and the county within the for loop, would achieve something like this. Moreover, if there was more demographics associated with the ballot information--this data could be greatly expanded to give users a more detailed view of the voting data. Someone would have to extract the demographic from the .csv and then build the code for what they are looking for.

### Notes

Using python to emphasize much of the data pertaining to each candidate made easy work of sifting through the .csv, and iterating through the data for each candidate's votes, as well as aggragating the votes to be assigned to one candidate and find the totals. Using for loops, a lot of the tabulations were able to be done synchronously, as well as calculating and tabulating the data and writing it data to a .txt file.  
