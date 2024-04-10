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



four_of_a_kind = sort_list_list(four_of_a_kind,5)
four_of_a_kind = sort_list_list(four_of_a_kind,4) # 1,2,3,4 are the same
four_of_a_kind = sort_list_list(four_of_a_kind,3)
four_of_a_kind = sort_list_list(four_of_a_kind,2)
four_of_a_kind = sort_list_list(four_of_a_kind,1)
# print(four_of_a_kind)
full_house = sort_list_list(full_house,5) # 4,5 are the same
full_house = sort_list_list(full_house,4)
full_house = sort_list_list(full_house,3) # 1,2,3 are the same
full_house = sort_list_list(full_house,2)
full_house = sort_list_list(full_house,1)
# print(full_house)

# This method is not suitable for sorting three of a kind, two pairs, pair, or high card.
three_of_a_kind = sort_list_list(three_of_a_kind,5)
three_of_a_kind = sort_list_list(three_of_a_kind,4)
three_of_a_kind = sort_list_list(three_of_a_kind,3) # 1,2,3 are the same
three_of_a_kind = sort_list_list(three_of_a_kind,2)
three_of_a_kind = sort_list_list(three_of_a_kind,1)
#print(three_of_a_kind)
two_pairs = sort_list_list(two_pairs,5)
two_pairs = sort_list_list(two_pairs,4) # 4,3 are the same
two_pairs = sort_list_list(two_pairs,3)
two_pairs = sort_list_list(two_pairs,2) # 1,2 are the same
two_pairs = sort_list_list(two_pairs,1)
# print(two_pairs)
one_pair = sort_list_list(one_pair,5)
one_pair = sort_list_list(one_pair,4)
one_pair = sort_list_list(one_pair,3)
one_pair = sort_list_list(one_pair,2) # 1,2 are the same
one_pair = sort_list_list(one_pair,1)
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
    print('rank: ',rank,' cards: ',hand[0],' bid: ',bid)
    hand_winnings = rank * hand[1]
    total_winnings += hand_winnings

print('number of lines processed: ',rank)
print(f"total_winnings: {total_winnings}")
'''
The lowest ranked hands will be 23456, 23457, 23458
The highest ranks will be AAAAA, AAAAJ, AAAJJ, ...      ..., QQQQJ, QQQJJ, QQJJJ, QJJJJ, TTTTT, ...


'''