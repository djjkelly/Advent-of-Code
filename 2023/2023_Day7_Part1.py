#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

folder = '2023/'
filename = '2023_Day7_input'
extension = '.txt'
full_path = folder + filename + extension

with open(full_path) as file_object: # test_input should give a total_winnings of 6440: done
    file_content = file_object.readlines()

# a rank of 1 means the weakest hand

card_ranking = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
reverse_card_ranking = card_ranking[::-1]
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

def sort_list_list(input_list,input_int):
    output_list = []
    for card in card_ranking:
        for line in input_list:
            if line[0][input_int]== card:
                output_list.append(line)
    return output_list

for j,line in enumerate(file_content):
    hand = line.split()[0]
    bid = int(line.split()[1])
    #print("line index: ", index,", hand: ",hand,", bid: ",bid)
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1
    #print(cards)
    values_list = list(cards.values())
    max_value = max(values_list)
    #print("max value: ",max_value)
    #cards["line index"] = index
    if max_value == 5:
        five_of_a_kind.append([hand,bid])
    elif max_value == 4:
        four_of_a_kind.append([hand,bid])
    elif max_value == 3:
        if 2 in values_list:
            full_house.append([hand, bid])
        else:
            three_of_a_kind.append([hand,bid])
    elif max_value == 2:
        if values_list.count(2) == 2:
            two_pairs.append([hand,bid])
        else:
            one_pair.append([hand,bid])
    else:
        high_card.append([hand,bid])
#print('5 of a kind: ',five_of_a_kind,'\n4 of a kind: ',four_of_a_kind,'\nfull house: ',full_house,'\n3 of a kind: ',three_of_a_kind,'\n2 pair: ',two_pairs,'\n1 pair: ',one_pair,'\nhigh card: ',high_card)

for i in [4,3,2,1,0]:
    four_of_a_kind = sort_list_list(four_of_a_kind,i)
    full_house = sort_list_list(full_house,i)
    three_of_a_kind = sort_list_list(three_of_a_kind,i)
    two_pairs = sort_list_list(two_pairs,i)
    one_pair = sort_list_list(one_pair,i)
    high_card = sort_list_list(high_card,i)

total_winnings = 0
all_hands = high_card + one_pair + two_pairs + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
for i, hand in enumerate(all_hands):
    rank = i + 1
    bid = hand[1]
    #print('rank: ',rank,' cards: ',hand[0],' bid: ',bid)
    hand_winnings = rank * hand[1]
    total_winnings += hand_winnings

print('number of lines processed: ',rank)
print(f"total_winnings: {total_winnings}")
'''
The lowest ranked hands will be 23456, 23457, 23458
The highest ranks will be AAAAA, KKKKK, QQQQQ...

I think my program needs to sort them into categories first, and then sort the categories.

251328559 answer submitted - wrong answer, too low.
251327055 answer submitted - wrong answer, too low. The sort_string function is not working correctly.
251603392 answer submitted - wrong answer, too low. Issue found in calling the sort_list function for four_of_a_kind.
251606919 answer submitted - wrong answer, too low. Issue found in calling the sort_list function for full_house.
251610788 answer submitted - wrong answer, too low. I've checked the logic of calling sort_list for other lists.
251806792 answer correct! - I misunderstood the secondary ranking requirements.
'''
test_dictionary = {
    '2023_Day7_input':
    {'answer':251806792},
}

from testmodule import test_function
test_function(test_dictionary,filename,total_winnings)