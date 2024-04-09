#!/usr/bin/env python3
#https://adventofcode.com/2023/day/7

with open("2023/2023_Day7_input.txt") as file_object: # test_input should give a total_winnings of 6440: done
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
            if line[0][input_int-1]== card:
                output_list.append(line)
    return output_list

def sort_string(string):
    char_counts = {}
    #print(string)
    string = ''.join(sorted(hand, key = lambda card: reverse_card_ranking.index(card)))
    print(string)
    four_cards,three_cards,two_cards = '','',''
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
            if char_counts[char] == 5:
                return string
        else:
            char_counts[char] = 1
    if char_counts[char] == 4:
        four_cards = char
        print('four cards: ',four_cards)
    if char_counts[char] == 3:
        three_cards = char
        print('three cards: ',three_cards)
    if char_counts[char] == 2:
        two_cards += char
        print('two cards: ',two_cards)
    repeated_chars = []
    unique_chars = ""
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars.append((char * count, count))
        else:
            unique_chars += char
    repeated_chars.sort(key=lambda x: reverse_card_ranking.index(x[0][0]))
    sorted_string = ''.join(group[0] for group in repeated_chars) + unique_chars
    return sorted_string

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
        five_of_a_kind.append([sort_string(hand),bid])
    elif max_value == 4:
        four_of_a_kind.append([sort_string(hand),bid])
    elif max_value == 3:
        if 2 in values_list:
            full_house.append([sort_string(hand), bid])
        else:
            three_of_a_kind.append([sort_string(hand),bid])
    elif max_value == 2:
        if values_list.count(2) == 2:
            two_pairs.append([sort_string(hand),bid])
        else:
            one_pair.append([sort_string(hand),bid])
    else:
        high_card.append([sort_string(hand),bid])
#print('5 of a kind: ',five_of_a_kind,'\n4 of a kind: ',four_of_a_kind,'\nfull house: ',full_house,'\n3 of a kind: ',three_of_a_kind,'\n2 pair: ',two_pairs,'\n1 pair: ',one_pair,'\nhigh card: ',high_card)

five_of_a_kind = sort_list_list(five_of_a_kind,5)
# print(five_of_a_kind)
four_of_a_kind = sort_list_list(four_of_a_kind,1)
four_of_a_kind = sort_list_list(four_of_a_kind,4)
# print(four_of_a_kind)
full_house = sort_list_list(full_house,2)
full_house = sort_list_list(full_house,3)
# print(full_house)

# This method is not suitable for sorting three of a kind, two pairs, pair, or high card.
three_of_a_kind = sort_list_list(three_of_a_kind,5)
three_of_a_kind = sort_list_list(three_of_a_kind,4)
three_of_a_kind = sort_list_list(three_of_a_kind,3)
#print(three_of_a_kind)
two_pairs = sort_list_list(two_pairs,5)
two_pairs = sort_list_list(two_pairs,4) # could also be based on 3
two_pairs = sort_list_list(two_pairs,2) # could also be based on 1
# print(two_pairs)
one_pair = sort_list_list(one_pair,5)
one_pair = sort_list_list(one_pair,4)
one_pair = sort_list_list(one_pair,3)
one_pair = sort_list_list(one_pair,2)
# print(one_pair)
high_card = sort_list_list(high_card,5)
high_card = sort_list_list(high_card,4)
high_card = sort_list_list(high_card,3)
high_card = sort_list_list(high_card,2)
high_card = sort_list_list(high_card,1)
# print(high_card)

total_winnings = 0
all_hands = high_card + one_pair + two_pairs + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
for i, hand in enumerate(all_hands):
    rank = i + 1
    bid = hand[1]
    #print('cards: ',hand[0],'bid: ',bid)
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
'''