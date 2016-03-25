#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    #print ">>> outlierCleaner start."

    for i in range(len(ages)):
        error = (net_worths[i] - predictions[i])**2
        cleaned_data.append([ages[i], net_worths[i], error])

    #print "cleaned_data=", cleaned_data
    cleaned_data.sort(key=lambda tup: tup[2])
    n = int(len(cleaned_data) * 0.9)
    cleaned_data = cleaned_data[:n]
    print "len(cleaned_data)", len(cleaned_data)
    return cleaned_data


    return cleaned_data
