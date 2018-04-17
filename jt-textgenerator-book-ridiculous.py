# New Love Songs from a Boyband? 
# Takes lyrics from the chorus's Top 40 'NSYNC songs 
# and randomly generates songs/poems....
# Jonathan Thomas, 2018
# Thanks to 'NSYNC

import random, textwrap
print "\nRandomly Generated 'NSYNC SONGS!\n\n"
text = ["Why don't you be my girlfriend",
"I'll treat you good",
"I know you hear your friends when they say you should",
"'Cause if you were my girlfriend",
"I'd be your shining star",
"The one to show you where you are",
"Girl you should be my girlfriend",
"Your love is like a river",
"Peaceful and deep",
"Your soul is like a secret",
"When I look into your eyes",
"I know that it's true",
"God must have spent...",
"A little more time",
"On you...",
"You're gone..",
"You're gone...you're gone.. you're....",
"You're all I ever wanted",
"You're all I ever needed--yeah",
"So tell me what to do now",
"When I want you back",
"'Cause I want you back",
"Every little thing I do",
"Never seems enough for you",
"You don't wanna lose it again",
"But I'm not like them",
"Baby--when you finally",
"Get to love somebody",
"Guess what",
"It's gonna be me..",
"Just close your eyes",
"Each loving day",
"I know this feeling won't go away",
"Till the day my life is through",
"This I promise you",
"Take it from me",
"It's a lesson to be learned",
"Even the good guys get burned",
"Take it from me",
"See I would give you love",
"The kind of love that you've only dreamed of",
"Baby you're not the only one",
"You don't have to be afraid to fall in love",
"And I know that you've hurt in the past",
"But if you want it--here's my heart",
"No strings attached",
"To see you give",
"Love and attention at his will",
"And you can't imagine how it makes me feel",
"To see you with him",
"Oh, it makes me ill"]

while len(text) > 5:
    random.shuffle(text)
    text.remove(random.choice(text))
    random.shuffle(text)
print "" + \
    textwrap.fill(", ".join(text) + "." + "\n", 80)
