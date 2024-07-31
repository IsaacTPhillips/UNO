def play_UNO(center_card, player_hands, curr_player_results, center_color, center_val):
    
    what_played = []
    cardPickUp = 0
    cardsPlayed = 0
    for player in range(num_players):
        #split the center card into color and val for comparisons
        #center_color, center_val = center_card[-1]
        #check through each card to compare to the center card
        for hand in player_hands:
            play_allow = 7
            card_pos = 0
            if len(hand) == 0:
                return False
            else:
                for card in hand:
                    card_pos += 1
                    if len(hand) < play_allow: 
                        break
                    if len(hand) == 0:
                        break
                    print(card)
                    for mid in center_card:
                        #if the center card has a plus two or plus four, add those cards to hand
                        if mid[0][1][-1] == 'PlusTwo':
                            hand +=  drawCards(2)
                            cardPickUp += 2
                        elif mid[0][1][-1] == 'Four':
                            hand +=  drawCards(4)
                            cardPickUp += 4
                        #Compare the cards and find out if you can play or if you have to draw
                        if mid[0][0][-1] == 'Wild':
                            #what_played.append(hand[card_pos-1])
                            center_card.append(hand.pop(card_pos-1))
                            card_pos -= 1
                            play_allow -= 1
                            cardsPlayed += 1
                        #for now this will also play skips and reverses with no heppening
                        #first color
                        elif (mid[0][0][-1] == card[0]) and (mid[0][0][-1] != 'Wild'):
                            #what_played.append(hand[card_pos-1])
                            center_card.append(hand.pop(card_pos-1))
                            card_pos -= 1
                            play_allow -= 1
                            cardsPlayed += 1
                        #Then value
                        elif (mid[0][1][-1] == card[1]):
                            #what_played.append(hand[card_pos-1])
                            center_card.append(hand.pop(card_pos-1))
                            card_pos -= 1
                            play_allow -= 1
                            cardsPlayed += 1
                        #If not value then we play any regular wild we have
                        elif (card[0] == 'Wild' and card[1] == "Wild"):
                            #what_played.append(hand[card_pos-1])
                            center_card.append(hand.pop(card_pos-1))
                            card_pos -= 1
                            play_allow -= 1
                            cardsPlayed += 1
                        #And if all else fails and we have no other card to play but the plus four
                        #we play the plus four. There is not change in color 
                        elif(card[0] == 'Wild') and (card[1] == 'Four'):
                            #what_played.append(hand[card_pos-1])
                            center_card.append(hand.pop(card_pos-1))
                            card_pos -= 1
                            play_allow -= 1
                            cardsPlayed += 1
                        

                        else:
                            hand += drawCards(1)
                            cardPickUp += 1
                            card_pos += 1
                            #break
                        print(center_card)
                    

        
        return cardPickUp, cardsPlayed, color_dict, what_played