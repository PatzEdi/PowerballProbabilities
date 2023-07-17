# PowerballProbabilities
 Powerball Lottery Data Probability loader and Parser written in Python

**Thank you Ac31415 for starring the repository!**

## Update:

Please note that initial release contained wrong information. I had fogotten to filter out certain results before/after some reformatting Powerball had made on their numbers. Now, all numbers before October 4, 2015 are filtered out, as on that date, Powerball changed their ranges from 1-59 to 1-69 for the normal white balls, and 1-35 to 1-26 for the Powerball. I had forgotten to filter out those before the specific date, leading to incorrect (biased) probabilities. The below information is correct, though, and it is based on the data taken from October (7th, the first ticket after format changes), 2015, up until present day. Apologies for the inconvenience.

## Usage

This project can be used to determine the probabilites of each number through the past decade or so of powerball winning ticket extractions. Note that the probabilities are extracted from October 4th, 2015 and up due to format changes. More information on that above.

You can enter the path in the variable **lottery_dataset_path** that leads to the lottery.txt file, which can be downloaded from [here](https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010). Download the csv, and change the extension from csv to txt.

Put the path to the file that gets created in the end with all the data in the **parsed_data_save_path** variable.

Run the script. The outputted file will contain something like this:


```

Lottery Number Probabilities from 2010 to 2023 (Greatest to Least Probabilities) (Filtered October 4th, 2015 and Up: Format Changes)
Number: 61 , Probability: 1.9469026548672566
Number: 32 , Probability: 1.8805309734513276
Number: 21 , Probability: 1.836283185840708
Number: 36 , Probability: 1.8141592920353982
Number: 63 , Probability: 1.7699115044247788
Number: 23 , Probability: 1.7699115044247788
Number: 69 , Probability: 1.7477876106194692
Number: 39 , Probability: 1.6592920353982303
Number: 59 , Probability: 1.6592920353982303
Number: 62 , Probability: 1.6371681415929202
Number: 64 , Probability: 1.6371681415929202
Number: 37 , Probability: 1.6150442477876108
Number: 47 , Probability: 1.592920353982301
Number: 3 , Probability: 1.592920353982301
Number: 28 , Probability: 1.592920353982301
Number: 33 , Probability: 1.592920353982301
Number: 53 , Probability: 1.5707964601769913
Number: 20 , Probability: 1.5707964601769913
Number: 27 , Probability: 1.5265486725663717
Number: 56 , Probability: 1.5265486725663717
Number: 68 , Probability: 1.5265486725663717
Number: 2 , Probability: 1.5265486725663717
Number: 15 , Probability: 1.5265486725663717
Number: 17 , Probability: 1.5265486725663717
Number: 10 , Probability: 1.5044247787610618
Number: 16 , Probability: 1.5044247787610618
Number: 44 , Probability: 1.4823008849557522
Number: 67 , Probability: 1.4823008849557522
Number: 6 , Probability: 1.4823008849557522
Number: 45 , Probability: 1.4823008849557522
Number: 52 , Probability: 1.4380530973451326
Number: 57 , Probability: 1.4380530973451326
Number: 18 , Probability: 1.4380530973451326
Number: 54 , Probability: 1.4380530973451326
Number: 66 , Probability: 1.415929203539823
Number: 12 , Probability: 1.415929203539823
Number: 19 , Probability: 1.415929203539823
Number: 40 , Probability: 1.415929203539823
Number: 50 , Probability: 1.3938053097345133
Number: 55 , Probability: 1.3938053097345133
Number: 14 , Probability: 1.3938053097345133
Number: 30 , Probability: 1.3938053097345133
Number: 58 , Probability: 1.3938053097345133
Number: 22 , Probability: 1.3938053097345133
Number: 38 , Probability: 1.3716814159292035
Number: 8 , Probability: 1.3716814159292035
Number: 11 , Probability: 1.3716814159292035
Number: 41 , Probability: 1.3716814159292035
Number: 31 , Probability: 1.3495575221238938
Number: 42 , Probability: 1.3495575221238938
Number: 1 , Probability: 1.3274336283185841
Number: 7 , Probability: 1.3053097345132743
Number: 24 , Probability: 1.3053097345132743
Number: 48 , Probability: 1.3053097345132743
Number: 65 , Probability: 1.3053097345132743
Number: 5 , Probability: 1.2831858407079646
Number: 43 , Probability: 1.2831858407079646
Number: 9 , Probability: 1.2831858407079646
Number: 51 , Probability: 1.261061946902655
Number: 60 , Probability: 1.261061946902655
Number: 29 , Probability: 1.238938053097345
Number: 35 , Probability: 1.2168141592920354
Number: 46 , Probability: 1.2168141592920354
Number: 4 , Probability: 1.1946902654867257
Number: 25 , Probability: 1.1946902654867257
Number: 49 , Probability: 1.1725663716814159
Number: 26 , Probability: 1.1504424778761062
Number: 34 , Probability: 1.1061946902654867
Number: 13 , Probability: 1.0398230088495575

Sum of Probabilities (Numbers): 100.00000000000003


Powerball Numbers
Powerball: 24, Powerball Probability: 5.199115044247788
Powerball: 18, Powerball Probability: 5.0884955752212395
Powerball: 4, Powerball Probability: 4.977876106194691
Powerball: 14, Powerball Probability: 4.424778761061947
Powerball: 26, Powerball Probability: 4.20353982300885
Powerball: 11, Powerball Probability: 4.20353982300885
Powerball: 25, Powerball Probability: 4.092920353982301
Powerball: 3, Powerball Probability: 3.982300884955752
Powerball: 6, Powerball Probability: 3.982300884955752
Powerball: 10, Powerball Probability: 3.982300884955752
Powerball: 13, Powerball Probability: 3.8716814159292032
Powerball: 19, Powerball Probability: 3.8716814159292032
Powerball: 21, Powerball Probability: 3.8716814159292032
Powerball: 5, Powerball Probability: 3.761061946902655
Powerball: 8, Powerball Probability: 3.761061946902655
Powerball: 9, Powerball Probability: 3.650442477876106
Powerball: 1, Powerball Probability: 3.5398230088495577
Powerball: 7, Powerball Probability: 3.5398230088495577
Powerball: 17, Powerball Probability: 3.4292035398230087
Powerball: 2, Powerball Probability: 3.4292035398230087
Powerball: 20, Powerball Probability: 3.4292035398230087
Powerball: 22, Powerball Probability: 3.3185840707964607
Powerball: 12, Powerball Probability: 3.2079646017699117
Powerball: 23, Powerball Probability: 3.2079646017699117
Powerball: 15, Powerball Probability: 2.9867256637168142
Powerball: 16, Powerball Probability: 2.9867256637168142

Sum of Probabilities (Powerball): 99.99999999999999

```

## How It Works

1. Gets the data from the file linked above (lottery data) using regex.
2. Splits the first five numbers from the last (differentiate between normal numbers and powerball)
3. Appends each number from the two categories to get a list of all numbers put together (used later on to count probability).
4. Creates a vocab for each of the lists containing all numbers (one for the normal 5 numbers, one for powerball numbers), by using **set** on the lists.
5. Iterates through each number in the vocab (first, for the first 5 numbers), and for each number, iterates through each number in the total numbers list. If the integer iterated through the total numbers list is equal to the number in the vocab, a count adds 1.
6. Probability is calculated by dividing the counter by the total number amount.
7. The numbers are then associated and ordered in order from greatest to least with a number and their matching probabily. So, the numbers at the top are the most probable.

## User Notice
- I am not responsible for any damage caused by the data above.
- The data is not used for any reason to cause a question towards Powerball and their reputation, concerning bias in their numbers, but it can of course be of use to you if you are researching such a topic ;)

## Credits:


 - https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010 Thank you State of New York for the data, very helpful!
