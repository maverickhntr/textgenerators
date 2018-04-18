# -*- coding: utf-8 -*-

# Transline Poem 
# Takes PeterParker/Spider-Man lines 
# and generates transline poems....
# Jonathan Thomas, 2018
# Thanks to Marvel Comics/Marvel Studios

import random
print "\nGreat Responsibility\n\n"
text = ["Well, I mean, I'd rather just stay on the ground for a little while",
"Did anyone call for a web-slinger?",
"Friendly neighborhood Spider-Man",
"Somebody's got to look out for the little guy, right?",
"Just a typical homecoming...on the outside of an invisible jet...fighting my girlfriend's dad",
"Come on, Peter.",
"Come on, Spider-Man",
"Come on, Spider-Man",
"Come on, Spider-Man",
"Come on, Spider-Man!",
"If you're nothing without this suit, then you shouldn't have it",
"Your friendly neighbourhood Spiderman!",
"S... Spider-Man",
"It's not a onesie!",
"You know what I think is really cool? This webbing. Tensile strength is off the charts. Who manufactured it?--I did", 
"It's just that... when...whatever happened happened, it's like my senses have been dialed to 11",
"I’ve been me my whole life…and I’ve had these powers for six months",
"When you can do the things that I can, but you don't... and then the bad things happen, they happen because of you",
"Yeah just looking out for the little guy. That's-That's what it is",
"I'm-I'm being serious! I can't just drop out of school! ",
"Don't tell Aunt May",
"I am responsible-- Oh, crap.-- My backpack's gone",
"With great power, comes great responsibility!",
"Are you an Avenger--Yeah, basically",
"This is so awesome",
"Who are these guys?",
"You have the right to remain silent!",
"Yikes, sorry. My bad",
"You'd never see that much action on a cartoon!",
"Oh great... Do you know how much it costs to dry clean this costume?",
"Boy! This hero stuff is just never easy!",
"Look out! Here comes the Spider-Man!",
"This is my chance to prove myself",
"They're in the middle of a heist. I could catch them red-handed",
"This is awesome",
"What's wrong with my web-shooters?",
"Hah. You deserve that. You're a criminal",
"Bye, Mr. Criminal",
"You're wrong, you think you're right...and it makes you dangerous.",
"If May finds out people try and kill me every night, she won't let me do this"]

action = ["bam",
"Bang",
"Ouch",
"Whack",
"wham",
"Thwick",
"Twisp"]
#These could also be the translines, I suppose.

taunt = ["Spider-Sense's tingling!",
"C'mon!",
"Bring it on!",
"Showtime!"]



selectedwords = []
repeats = []
repeats.append(random.choice(["With great power, comes great responsibility!", "When you can do the things that I can, but you don't... and then the bad things happen, they happen because of you", "Yeah just looking out for the little guy. That's-That's what it is"])) 

text.remove(repeats[0])

j = 2 * random.randint(10, 15)
j = int(j)


i = 0
while (i < j):
    paragraph = []
    random.shuffle(text)
    paragraph.append(random.choice(text))
    paragraph.append(random.choice(text))
    paragraph.append(random.choice(text))
    selectedwords.append(paragraph)
    random.shuffle(text)
    i += 1

k = random.randint(1, 10)
k = int(k)


i = 0
while (i < k):
    print("\n" + selectedwords[i][0] + ",")
    test = random.randint(5, 100)
    if(test % 5 ==0):
        battle = random.choice(action)
        print("--" + battle.upper() + "!! --")
    print(selectedwords[i][1] + ",") 
    if(test % 7 ==0):
        yell = random.choice(taunt)
        print(yell + "!!")    
    if(test % 6 ==0):
        battle = random.choice(action)
        print("--" + battle.upper() + "!! --")
    print(selectedwords[i][2] + ".")
    print(repeats[0] + "\n") 
    i += 1
 
 

