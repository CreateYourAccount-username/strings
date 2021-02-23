# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
scorer_name0 = 'Ruud Gullit'
scorer_name1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_name0 + ' ' + str(goal_0) + ', ' + scorer_name1 + ' ' + str(goal_1)
report = f'{scorer_name0} scored in the {goal_0}nd minute\n{scorer_name1} scored in the {goal_1}th minute'

# Part 2
player = 'Oleksiy Mykhaylychenko'
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find(' ') + 1:])
name_short = str(player[0] + '. ' + player[player.find(' ') + 1:])
chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!')
good_chant = chant[-1] != ' '