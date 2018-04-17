# Transline Poem 
# Takes PeterParker/Spider-Man lines 
# and generates transline poems....
# Jonathan Thomas, 2018
# Thanks to Marvel Comics/Marvel Studios

import random
print "\nSpider-Man: Year One - In Peter Parker's Mind\n\n"
text = ["Well, I mean, I'd rather just stay on the ground for a little while",
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
"Are you an Avenger--Yeah, basically",
"This is so awesome",
"Who are these guys?",
"You have the right to remain silent!",
"Yikes, sorry. My bad",
"Spider-Sense's tingling!",
"You'd never see that much action on a cartoon!",
"Showtime!",
"Oh great... Do you know how much it costs to dry clean this costume?",
"Boy! This hero stuff is just never easy!",
"Look out! Here comes the Spider-Man!",
"This is my chance to prove myself",
"They're in the middle of a heist. I could catch them red-handed",
"This is awesome",
"What's wrong with my web-shooters?",
"Hah. You deserve that. You're a criminal",
"Bye, Mr. Criminal",
"If May finds out people try and kill me every night, she won't let me do this"]

selectedwords = []
repeats = []

random.shuffle(text)
repeats.append(random.choice(text))
text.remove(repeats[0])
random.shuffle(text)

    
#consider keeping the lasat line constant. maybe an infinite poem?
#"With great power, comes great responsibility."
#"If you're nothing without the suit, then you shouldn't have it."
#"When you can do the things that I can, and then the bad things happen, they happen because of you."
#add serialization.
#

i = 0
while (i < 3):
    paragraph = []
    random.shuffle(text)
    paragraph.append(random.choice(text))
    text.remove(paragraph[0])
    paragraph.append(random.choice(text))
    text.remove(paragraph[1])
    paragraph.append(random.choice(text))
    text.remove(paragraph[2])
    selectedwords.append(paragraph)
    random.shuffle(text)
    i += 1

print("\n" + selectedwords[0][0] + ",")  
print(selectedwords[0][1] + ", --" + repeats[0] +  "--") 
print(selectedwords[0][2] + ". \n") 
print(selectedwords[1][0] + ",") 
print(selectedwords[1][1] + ", --" + repeats[0] + "--") 
print(selectedwords[1][2] + ". \n") 
print(selectedwords[2][0] + ",") 
print(selectedwords[2][1] + ", --" + repeats[0] + "--") 
print(selectedwords[2][2] + ". \n") 
 

