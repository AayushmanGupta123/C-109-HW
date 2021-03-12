import random
import statistics
import plotly.graph_objects as px
dice = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)

mean = sum(dice)/len(dice)
std_dev = statistics.stdev(dice)
median = statistics.median(dice)
mode = statistics.mode(dice)
##print("mean = "+str(mean))
##print("std_dev = "+str(std_dev))
##print("median = "+str(median))
##print("mode = "+str(mode))
first_std_start,first_std_end = mean-std_dev,mean+std_dev
list_of_data_within_1_std_deviation = [result for result in dice if result > first_std_start and result < first_std_end]
second_std_start,second_std_end = mean-(2*std_dev),mean+(2*std_dev)
list_of_data_within_2_std_deviation = [result for result in dice if result > second_std_start and result < second_std_end]
third_std_start,third_std_end = mean-(3*std_dev),mean+(3*std_dev)
list_of_data_within_3_std_deviation = [result for result in dice if result > third_std_start and result < third_std_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice)))
fig = px.create_distplot([dice], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
#fig = px.create_distplot([dice],["Result"])
#fig.show()