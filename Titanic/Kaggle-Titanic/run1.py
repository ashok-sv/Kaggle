# importing required packages
import csv as csv
import numpy as np

# importing data and populating array
csv_file_object = csv.reader(open('../train.csv', 'rb'))
header = csv_file_object.next()
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

# importing test data
test_file = open('../test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

# creating pointer to output file
gender_prediction_file = open("genderbasedmodel2.csv", "wb")
gender_prediction_file_object = csv.writer(gender_prediction_file)

# quick check that data is correct
print data

# working out survival proportion
number_passengers = np.size(data[0::, 1].astype(np.float))
number_survived = np.sum(data[0::, 1].astype(np.float))
proportion_survived = number_survived / number_passengers
print "Proportion of survivors: " + str(proportion_survived)

# basic gender filtering
women_only_stats = data[0::, 4] == "female"
men_only_stats = data[0::, 4] == "male"

women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print("Proportion of women who survived: " + str(proportion_women_survived))
print("Proportion of men who survived: " + str(proportion_men_survived))

gender_prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:
    if row[3] == 'female':
        gender_prediction_file_object.writerow([row[0], '1'])
    else:
        gender_prediction_file_object.writerow([row[0], '0'])
test_file.close()
gender_prediction_file.close()