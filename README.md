# PowerballProbabilities
 Powerball Lottery Data Probability loader and Parser written in Python


## Usage

This project can be used to determine the probabilites of each number through the past decade or so of powerball winning ticket extractions.

You can enter the path in the variable **lottery_dataset_path** that leads to the lottery.txt file, which can be downloaded from [here](https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010). Download the csv, and change the extension from csv to txt.

Put the path to the file that gets created in the end with all the data in the **parsed_data_save_path** variable.

Run the script. The outputted file will contain something like this:


```

Lottery Number Probabilities from 2010 to 2023 (Greatest to Least Probabilities):

Number: 36 , Probability: 1.8498659517426272
Number: 39 , Probability: 1.8230563002680964
Number: 32 , Probability: 1.8096514745308312
Number: 23 , Probability: 1.7828418230563001
Number: 28 , Probability: 1.7158176943699734
Number: 59 , Probability: 1.7158176943699734
Number: 21 , Probability: 1.7024128686327078
Number: 10 , Probability: 1.675603217158177
Number: 20 , Probability: 1.6487935656836463
Number: 45 , Probability: 1.6487935656836463
Number: 54 , Probability: 1.6487935656836463
Number: 11 , Probability: 1.6353887399463807
Number: 14 , Probability: 1.621983914209115
Number: 17 , Probability: 1.621983914209115
Number: 41 , Probability: 1.621983914209115
Number: 52 , Probability: 1.621983914209115
Number: 12 , Probability: 1.6085790884718498
Number: 47 , Probability: 1.6085790884718498
Number: 3 , Probability: 1.5951742627345844
Number: 22 , Probability: 1.5951742627345844
Number: 33 , Probability: 1.5549597855227881
Number: 37 , Probability: 1.5549597855227881
Number: 40 , Probability: 1.5549597855227881
Number: 44 , Probability: 1.5549597855227881
Number: 8 , Probability: 1.5549597855227881
Number: 16 , Probability: 1.5549597855227881
Number: 19 , Probability: 1.5415549597855227
Number: 55 , Probability: 1.5415549597855227
Number: 53 , Probability: 1.5281501340482573
Number: 56 , Probability: 1.5281501340482573
Number: 2 , Probability: 1.514745308310992
Number: 7 , Probability: 1.514745308310992
Number: 38 , Probability: 1.514745308310992
Number: 57 , Probability: 1.5013404825737267
Number: 18 , Probability: 1.5013404825737267
Number: 27 , Probability: 1.5013404825737267
Number: 30 , Probability: 1.5013404825737267
Number: 58 , Probability: 1.5013404825737267
Number: 31 , Probability: 1.487935656836461
Number: 48 , Probability: 1.4745308310991956
Number: 1 , Probability: 1.4745308310991956
Number: 6 , Probability: 1.4611260053619302
Number: 15 , Probability: 1.4611260053619302
Number: 49 , Probability: 1.447721179624665
Number: 5 , Probability: 1.447721179624665
Number: 50 , Probability: 1.447721179624665
Number: 9 , Probability: 1.447721179624665
Number: 51 , Probability: 1.4343163538873995
Number: 24 , Probability: 1.420911528150134
Number: 13 , Probability: 1.4075067024128687
Number: 29 , Probability: 1.3806970509383378
Number: 42 , Probability: 1.3806970509383378
Number: 4 , Probability: 1.3672922252010724
Number: 46 , Probability: 1.353887399463807
Number: 43 , Probability: 1.3404825737265416
Number: 25 , Probability: 1.3270777479892761
Number: 34 , Probability: 1.2868632707774799
Number: 26 , Probability: 1.2868632707774799
Number: 35 , Probability: 1.2868632707774799
Number: 61 , Probability: 1.1796246648793565
Number: 63 , Probability: 1.0723860589812333
Number: 69 , Probability: 1.0589812332439679
Number: 62 , Probability: 0.9919571045576407
Number: 64 , Probability: 0.9919571045576407
Number: 68 , Probability: 0.9249329758713136
Number: 67 , Probability: 0.8847184986595175
Number: 66 , Probability: 0.8445040214477211
Number: 65 , Probability: 0.7908847184986596
Number: 60 , Probability: 0.7640750670241286

Sum of Probabilities (Numbers): 100.00000000000003


Powerball Numbers:

Powerball: 24, Powerball Probability: 5.079605761940864
Powerball: 18, Powerball Probability: 4.776345716451857
Powerball: 4, Powerball Probability: 4.397270659590599
Powerball: 11, Powerball Probability: 4.245640636846096
Powerball: 14, Powerball Probability: 4.169825625473845
Powerball: 25, Powerball Probability: 4.169825625473845
Powerball: 5, Powerball Probability: 3.9423805913570886
Powerball: 19, Powerball Probability: 3.9423805913570886
Powerball: 26, Powerball Probability: 3.9423805913570886
Powerball: 6, Powerball Probability: 3.9423805913570886
Powerball: 8, Powerball Probability: 3.8665655799848366
Powerball: 10, Powerball Probability: 3.8665655799848366
Powerball: 7, Powerball Probability: 3.8665655799848366
Powerball: 13, Powerball Probability: 3.790750568612585
Powerball: 17, Powerball Probability: 3.7149355572403335
Powerball: 1, Powerball Probability: 3.7149355572403335
Powerball: 3, Powerball Probability: 3.7149355572403335
Powerball: 20, Powerball Probability: 3.639120545868082
Powerball: 23, Powerball Probability: 3.56330553449583
Powerball: 2, Powerball Probability: 3.4874905231235784
Powerball: 12, Powerball Probability: 3.4874905231235784
Powerball: 15, Powerball Probability: 3.4874905231235784
Powerball: 16, Powerball Probability: 3.411675511751327
Powerball: 22, Powerball Probability: 3.2600454890068233
Powerball: 9, Powerball Probability: 3.2600454890068233
Powerball: 21, Powerball Probability: 3.2600454890068233

Sum of Probabilities (Powerball): 100.00000000000001

```

## How It Works

1. Gets the data from the file linked above (lottery data) using regex.
2. Splits the first five numbers from the last (differentiate between normal numbers and powerball)
3. Appends each number from the two categories to get a list of all numbers put together (used later on to count probability).
4. Creates a vocab for each of the lists containing all numbers (one for the normal 5 numbers, one for powerball numbers), by using **set** on the lists.
5. Iterates through each number in the vocab (first, for the first 5 numbers), and for each number, iterates through each number in the total numbers list. If the integer iterated through the total numbers list is equal to the number in the vocab, a count adds 1.
6. Probability is calculated by dividing the total number amount by the counter.
7. The numbers are then associated and ordered in order from greatest to least with a number and their matching probabily. So, the numbers at the top are the most probable.

## User Notice
- I am not responsible for any damage cuased by the data above.
- The data is not used for any reason to cause a question towards Powerball and their reputation, concerning bias in their numbers, but it can of course be of use to you if you are researching such a topic ;)

## Credits:


 - https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010 Thank you State of New York for the data, very helpful!
