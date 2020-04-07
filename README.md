# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts: Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:

Q: What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

- A: Arrays are the most time and space efficient data structure, with a O(1) or constant time to access items inside an array. Under the hood arrays use a simple forumla composed of arithmetics operations `index * sizeof(type) + start_address`, computers can process this formula very very quickly as it's simple arithmetics hence the reason as to why arrays are O(1) to access items. 

- Adding to the beginning of an array is O(n) or linear time as you'll need to move each element down one, and if theres no space you'll also need to resize the array. 

- Removing items from an array is O(n) or linear time as you'll need to remove the item and move over the rest of the elements. 

- Inserting at the end of the array can be best O(1) or constant time if it has room, but average of O(n) as you'll need to resize the array.

Q: What is the worse case scenario if you try to extend the storage size of a dynamic array?

- A: Worst and best case of extending the storage size of an dynamic array is O(n).

Q: Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

- The blockchain is a datastructure and method of storing data that allows you to not have to trust anyone. Each block on the blockchain is a merely on object of data which includes an index, timestamp, list of transactions, proof used to mine said block, and cryptographic hash of the previous block. The hash of the previous block is a vital piece of data to store as it is what allows blocks to "chain" together creating the blockchain.

Q: Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

- Proof of work is a consensus algorithm that is used to deter DDOS attacks and other attacks such as spam on a network by requiring some work from the requesting client (typically mathematical puzzles), also known as a CPU cost function. POW protects the blockchain when adding new blocks or performing transaction by allowing other miners or nodes on the network to validate the proof of work by comparing hash nonces. However proof of work doesn't eliminate all attacks as the blockchain is still susceptible to 51% Attacks. My favorite definition of a 51% attack comes from binance (a crypto exchange).

      	
      	A 51% attack is a potential attack on a blockchain network, where a single entity or organization is able to control the majority of the hash rate, potentially causing a network disruption. In such a scenario, the attacker would have enough mining power to intentionally exclude or modify the ordering of transactions. They could also reverse transactions they made while being in control - leading to a double-spending problem.

      	A successful majority attack would also allow the attacker to prevent some or all transactions from being confirmed (transaction denial of service) or to prevent some or all other miners from mining, resulting in what is known as mining monopoly.

      	On the other hand, a majority attack would not allow the attacker to reverse transactions from other users nor to prevent transactions from being created and broadcasted to the network. Changing the block’s reward, creating coins out of thin air or stealing coins that never belonged to the attacker are also deemed as impossible events.

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

_You may not use any advanced, built-in Python functions to solve these problems._

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin. Keep in mind that with many people competing over the same coins, this may take a long time. By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)

### Rubric

| _OBJECTIVE_                                                                                                     | _TASK_             | _1 - DOES NOT MEET EXPECTATIONS_                                                     | _2 - MEETS EXPECTATIONS_                                                  | \*3 - EXCEEDS EXPECTATIONS                                                                                            |
| --------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\. | The student fully explains 4 or more items from the bulleted list\.                                                   |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.      | Tests pass on both problems. Solution utilizes a hash table.              | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints. |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\. | The student fully explains 4 or more items from the bulleted list\.                                                   |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                        | The student was able to mine a coin before the end of lunch.              | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\. | The student fully explains 4 or more items from the bulleted list\.                                                   |

## Grading

The grade for this sprint challenge is the average of the number of points received (points/15)
