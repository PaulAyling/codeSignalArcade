# QUESTION: For a given sequence can we have an increasing sequence by removing 1 record
# DEFINE:    EXAMPLES
# Increasing sequence           Not an increasing sequence
# 1,5,6,9                       1,3,2,1
# 1,2,3,4                       10,1,2,3

# difficult example : [ 1, 2, 7, 4, 5] 
def almostIncreasingSequence(sequence):
    print('sequence',sequence)
    def identifyNegativeIntervals(sequence):
        intervals = []
        intervals_negative_tally = []
        interval_neg_loc = []
        for n in range(len(sequence)-1):
            interval = sequence[n+1] - sequence[n]
            intervals.append(interval)
            #update the list of just negative intervals
            if intervals[n] < 1:  
                intervals_negative_tally.append(1)
                #THIS IS THE LAST THING THAT NEEDS FIXING
                location_of_neg = n
                interval_neg_loc.append(n) 
            nbr_neg_intervals = sum(intervals_negative_tally) 
            
        return {
            'interval_neg_loc':interval_neg_loc,
            'nbr_neg_intervals':nbr_neg_intervals,
            'intervals_negative_tally':intervals_negative_tally}
    
    negativeIntervals = identifyNegativeIntervals(sequence)
    interval_neg_loc = negativeIntervals['interval_neg_loc']
    nbr_neg_intervals = negativeIntervals['nbr_neg_intervals']
    intervals_negative = negativeIntervals['intervals_negative_tally']
    
    
    
    postition_neg_value = interval_neg_loc[0] + 1
    nbr_posotions_in_squence = len(sequence) - 1
    
    # print('postition_neg_value', postition_neg_value)
    # print('nbr_posotions_in_squence', nbr_posotions_in_squence)
    # print('interval_neg_loc', interval_neg_loc)
    # print('sequence length', len(sequence))
    # print('nbr_neg_intervals', nbr_neg_intervals)
    #remove outliers
    
    if nbr_neg_intervals > 1:
        can_be_sequenced = False
        print('More than 1 neg interval ', can_be_sequenced)
        return can_be_sequenced
    if interval_neg_loc[0] == 0: 
        print('zzzzzz')
        can_be_sequenced = True
        print('Neg interval at beginning', can_be_sequenced )
        return can_be_sequenced
    if postition_neg_value >= nbr_posotions_in_squence: 
        can_be_sequenced = True
        print('Neg interval at end', can_be_sequenced )
        return can_be_sequenced
        
   # print('*************************************************'
    # Evaluate main
    # eg in [1, 2, 7, 4, 5] 
    # value_before = 7.  value = 4. value_after = 5  
    print('postition_neg_value',postition_neg_value)
    value_before = sequence[postition_neg_value-1]   
    value = sequence[postition_neg_value]
    value_after = sequence[postition_neg_value+1]
    print('value_before',value_before)
    print('value',value)
    print('value_after',value_after)
    if value_after > value_before:
        can_be_sequenced = True
        print('If eroneous value removed: can_be_sequenced', can_be_sequenced )
        return can_be_sequenced
    elif value > 2:
        value_two_before =  sequence[postition_neg_value-2]  
        print('++++++++++++++++')
        print('value_two_before',value_two_before)
        if value > value_two_before:
            can_be_sequenced = True
            print('If value before negative is removed can be seqenced: can_be_sequenced', can_be_sequenced )
            return can_be_sequenced
        else:
            can_be_sequenced = False
            print('If value before negative is removed cannot be sequenced: can_be_sequenced', can_be_sequenced )
            return can_be_sequenced
    else:
        can_be_sequenced = False
        print('If you remove either the value or the one before: can_be_sequenced', can_be_sequenced )
        return can_be_sequenced
                