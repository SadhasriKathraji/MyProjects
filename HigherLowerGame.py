import text_ascii
import random
import os

print(text_ascii.game)
# create a list having multiple dictionaries
data = [
	{
		'name': 'Instagram',
		'follower_count': 346,
		'description': 'Social media platform',
		'country': 'United States'
	},
	{
		'name': 'Cristiano Ronaldo',
		'follower_count': 215,
		'description': 'Footballer',
		'country': 'Portugal'
	},
    {
		'name': 'Narendra Modi',
		'follower_count': 155,
		'description': 'Prime minister',
		'country': 'India'
	},
    {
		'name': 'dianxi',
		'follower_count': 5,
		'description': 'Youtuber',
		'country': 'China'
	},
    {
		'name': 'Gukesh',
		'follower_count': 121,
		'description': 'Chess Grandmaster',
		'country': 'India'
	},
    {
		'name': 'Jenny',
		'follower_count': 1,
		'description': 'Youtuber',
		'country': 'India'
	},
	{
		'name': 'Ariana Grande',
		'follower_count': 183,
		'description': 'Musician and actress',
		'country': 'United States'
	}
]

score = 0
random_item2 = random.choice(data)
continue_flag = True
while continue_flag:
    random_item1 = random_item2
    random_item2 = random.choice(data)
    while random_item1==random_item2:
        random_item2 == random.choice(data)

    print(f"Compare 1: {random_item1['name']}, {random_item1['description']}, from {random_item1['country']}")
    print(text_ascii.vs)
    print(f"Compare 2: {random_item2['name']}, {random_item2['description']}, from {random_item2['country']}")
    guess = int(input("Who has more followers? Type 1 or 2: "))


    followers_1 = random_item1['follower_count']
    followers_2 = random_item2['follower_count']

    def check(guess,followers_1,followers_2):
        if followers_1>followers_2 and guess == 1:
            return True
        elif followers_2>followers_1 and guess == 2:
            return True
        else:
            return False
    check_result = check(guess,followers_1,followers_2)
    #print(check_result)

    os.system('cls')
    print(text_ascii.game)
    if check_result:
        score += 1
        print(f"You are right. Your score is: {score}")
    else:
        continue_flag = False
        print(f"You are wrong. Your final score is:{score} ")




