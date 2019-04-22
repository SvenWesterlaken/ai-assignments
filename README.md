# Artificial Intelligence Assignments

## Appendix A – Determine emotional value of tweets

### Introduction
Twitter represents a fundamentally new instrument to make social measurements. Millions of people voluntarily express opinions across any topic imaginable. This data source is incredibly valuable for both research and business. For example, researchers have shown that the "mood" of communication on twitter reflects biological rhythms and can even be used to how Twitter moods predict the stock market.
In this assignment, you will:
•	access the twitter Application Programming Interface (API).
•	estimate the public's perception (the sentiment) of a particular term or phrase.
•	analyze the relationship between location and mood based on a sample of twitter data
Some points to keep in mind:
•	This assignment is open-ended in several ways. You'll need to make some decisions about how best to solve the problem and implement them carefully.
•	It is perfectly acceptable to discuss your solution, but don't share code.
•	Each student must submit his/her own solution to the problem.

### Twitter Application Programming Interface
Twitter provides a very rich REST API for querying the system, accessing data, and control your account. You can read more about the Twitter API here.

### Programming environment
This assignment has to be completed with the programming language Python.

### Step 1: Get Twitter Data
To access the live stream, you will need to install an oauth2 library so you can properly authenticate; choose a library appropriate for your programming environment. The steps below will help you set up your twitter account to be able to access the live stream.
1.	Create a twitter account if you do not already have one or you want to use a dedicated account for this assignment.
2.	Go to https://dev.twitter.com/apps and log in with your twitter credentials.
3.	Click "Create New App".
4.	Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5.	At this point you will be prompted to attach a mobile phone number to your account if you have not previously done so. Follow the instructions at the link provided. If you cannot complete this protocol, you may ask your instructor for the sample dataset in the repository, but it is encouraged you to connect to Twitter if possible so you can build your own applications.
6.	On the next page, click the "Keys and Access Tokens" tab along the top, then scroll all the way down until you see the section "Your Access Token".
7.	Click the button "Create My Access Token". You can Read more about Oauth authorization.
8.	You will probably need four values later. These values are your "Consumer Key (API Key)", your "Consumer Secret (API Secret)", your "Access token" and your "Access token secret". All should now be visible on the "Keys and Access Tokens" page. You may see "Consumer Key (API Key)" referred to as either "Consumer key" or "API Key" in some places in code or on the web; all three are synonyms.
Now that your keys are ready, you are ready to test your access:
•	Run your code and make sure you see data flowing and that no errors occur. Build up a file output.txt for the duration of the assignment; we will be reusing it in later problems. Don't use someone else's file; we will check for uniqueness in other parts of the assignment.
•	If you wish, modify the file to use the twitter search API to search for specific terms. For example, to search for the term "microsoft" or “apple”, you can pass the following url to the twitterreq function: https://api.twitter.com/1.1/search/tweets.json?q=microsoft. Is the sentiment on Microsoft or Apple, or any other company or topic, positive or negative?
Should you for any reason not be able to use to work with the live Twitter stream using the development API, you can instead use the dataset called JustSomeTweets, available from your instructor.

_Please note: You will use the data from this assignment in all other steps (2 – 5)._

### Step 2: Derive the sentiment of each tweet (2 points)
For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
Your program should accept two inputs: a sentiment file and a tweet file (like the one you generated in Assignment 1). The file SentimentScore.txt, available with the course material, contains a list of pre-computed sentiment scores . It is a list of English words rated for valence with an integer between minus five (negative) and plus five (positive). Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in this file should be given a sentiment score of 0. Note that the file is tab-delimited, meaning that term and score are separated by a tab character; a tab character generally can be identified by "\t".
The data in a tweet file is represented as JSON, which stands for JavaScript Object Notation. It is a simple format for representing nested structures of data, lists of lists of dictionaries of lists of ...., you get the idea. Each line of a tweet file represents a streaming message. Most, but not all, will be tweets. It is not too difficult to convert a JSON string into a data structure; you will probably find a library to do so.
You can read the Twitter documentation to understand what information each tweet contains and how to access it, but it's not too difficult to deduce the structure by direct inspection. Your program should produce an output file with the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on. If you sort the scores, they won't match up. If you sort the tweets, they won't match up. Once again: The nth line of the file you submit should contain only a single number that represents the score of the nth tweet in the input file!
NOTE: You must provide a score for every tweet in the sample file, even if that score is zero. You can assume the sample file will only include English tweets and no other types of streaming messages. Hint: This is real-world data, and it can be messy! Refer to the twitter documentation to understand more about the data structure you are working with. Don't get discouraged, and ask for help on the forums if you get stuck!

### Step 3: Compute Term Frequency
Write a program to compute a term frequency histogram of the livestream data you harvested. The frequency of a term can be calculated as [# of occurrences of the term in all tweets] / [# of occurrences of all terms in all tweets]
Your program should produce on each line of output should a term, followed by the frequency of that term in the entire file. There should be one line per unique term in the entire file. Even if 25 tweets contain the word lol, the term lol should only appear once in your output (and the frequency will be at least 25!) Each line should be in the format <term:string> <frequency:float>.
If you wish, you may consider a term to be a multi-word phrase, but this is not required. You may compute the frequencies of individual tokens only.
Depending on your method of parsing, you may end up computing frequencies for hashtags, links, stop words, phrases, etc. If you choose to filter out these non-words, that's ok too.

### Step 4: Which Origin is Happiest?
Write a program that returns the name of the happiest origin as a string. We define origin as the location of a tweet. Depending on your dataset this may be a city, country, state/province, continent, et cetera.
Your program should take a file of tweets as input. Assume the tweet file contains data formatted the same way as the livestream data. It's a good idea to make use of your solution to Assignment 2.
There are different ways you might assign a location to a tweet. Here are three:
•	Use the coordinates field (a part of the place object, if it exists), to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into an origin.
•	Use the other metadata in the place field. Much of this information is hand-entered by the twitter user and may not always be present or reliable, and may not typically contain an origin.
•	Use the user field to determine the twitter user's home origin. This location does not necessarily correspond to the location where the tweet was posted, but it's reasonable to use it as a proxy.
But you are free to develop your own strategy for determining the origin that each tweet comes from. You can ignore any tweets for which you cannot assign a location. Note: Not every tweet will have a text field; again, real data is dirty! Be prepared to debug, and feel free to throw out tweets that your code can't handle to get something working. For example, you might choose to ignore all non-English tweets.
Your program should print some name of the origin with the highest average tweet sentiment. Note that you may need a lot of tweets in order to get enough tweets with location data. Let the live stream run for a while if you wish.

### Step 5: Top ten hash tags
Write a program that computes the ten most frequently occurring hashtags from the data you gathered in Assignment 1.
In the tweet file, each line is a Tweet object, as described in the twitter documentation. To find the hashtags, you should not parse the text field; the hashtags have already been extracted by twitter.
Your script should produce each hashtag-count pair, one per line, in the following format:
a hashtag, followed by the frequency of that hashtag in the entire file. There should be one line per unique hashtag in the entire file. Each line should be in the format <hashtag:string> <frequency:float>.
