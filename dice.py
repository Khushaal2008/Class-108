import random
import plotly.express as px
import plotly.figure_factory as ff

count = []
dice_result=[]
for i in range(0,101):
    dice = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Dice 1: ",dice,"\nDice 2: ", dice2)
    dice_result.append(dice + dice2)
    count.append(i)
    print("Dice result is:", dice_result)
    print("Count:", count)

#fig = px.bar(x=dice_result, y=count)
fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
fig.show()