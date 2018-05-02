# GRE_VOCAB
Help you to remember  thesaurus and antonym of GRE vocabulary.

> In the CSV file, We have 100 groups words. All words in each group have the same meaning. It is paramount ability for a test taker to recognize those words.

This project will extract some words from two groups randomly each round.

You type  answer and the system will return a feedback.



### REQUIREMENTS

- python 3.6
- pandas 



### USAGE

```pyth
> cd src 
> python game.py
type the round you want to play!
>10
    ===round 1===
        0 indulgent    1 partisan    2 tendentious    3 partial
        4 deluxe    5 plush    6 baroque    7 unjust
    Meaning:主观偏见的
    type your answer:
>0 1 2 3
    You are wrong. Right answer is :1 2 3 7
    主观偏见的: tendentious unjust partial partisan
    奢华的: baroque indulgent plush deluxe
	===round 2===
    0 banal    1 prodigal    2 bromide    3 improvident
    4 stereotyped    5 dissolute    6 threadbare    7 sumptuous
	Meaning:浪费
	type your answer:
>3 5 7 1
You are right. Other words meaning is 陈腐的
```



### To-Do

- Add memory mechanism， help you to review words occured in the game.
- Add UI, maybe a web application is a good choice.