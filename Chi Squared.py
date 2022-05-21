def sum_of_dif_O_E_squared(list_of_numbers,length,expected_value):
    count=0
    sum_d_squared=0
    for count in range(length):
        d_squared=(list_of_numbers[count]-expected_value)**2
        print("Difference Squared",(count+1),":",d_squared)
        sum_d_squared=sum_d_squared+d_squared      
    return sum_d_squared
    
list_of_numbers=[12,15,43,63,11,34,0.234,0.00231,0.0000004]
length=len(list_of_numbers)
expected_value=sum(list_of_numbers)/len(list_of_numbers)
sum_of_difs_squared=sum_of_dif_O_E_squared(list_of_numbers,length,expected_value) #Expected value is the mean value at all plots.
test_statistic=sum_of_difs_squared/expected_value
print("Expected value:",expected_value)
print("Sum of the differences squared:",sum_of_difs_squared)
print("Test statistic:",round(test_statistic,4),"(4.d.p)")


