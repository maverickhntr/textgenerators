# -*- coding: utf-8 -*-
# Full Potential
# A 1k story generator (excluding comments) that uses only Action lines from The Matrix screenplay (pg. 112-113, 122-123)
# The Wolf/Wolves in place of the Agents, Little Red Riding hood in place of Neo
# Jonathan Thomas, 2018
# Thanks to Larry and Andy Wachowski


import random, textwrap
text = ['She looks at the dead escalator that rises up behind her.',
'Slowly she turns back and in her eyes we see something different, something fixed and hard like the resolve of a gunfighter.',
'There is no past or future in these eyes, only eternity.',
'Others are unable to understand.',
'What is she doing?, they ask',
'She is beginning to believe.',
'She whip-draws her gun with the flashpoint speed of lightning as The Wolf OPENS FIRE.',
'GUN REPORT THUNDERS through the underground, both of them BLASTING, moving at impossible speed.',
'For a blinking moment we enter BULLET-TIME.',
'Gun flash tongues curl from her gun, bullets float forward like a plane moving across the sky, cartridges cartwheel into space.',
'An instant later they are nearly on top of each other, rolling up out of a move that is almost a mirrored reflection of the other...',
'Each jamming their gun tight to the head of the other.',
'They freeze in a kind of embrace; her sweating, panting -- The Wolf ever so calm.',
'The Wolf smiles.',
'You are empty, the Wolf says. So are you, she replies.',
'The smile falls. She and The Wolf throw their guns aside.',
'Stand-off.',
'The face of the Wolf warps with rage and he attacks, fists flying at furious speed.', 
'A knife-hand opens the forearm of The Wolf, and a kick sends him slamming back against a steel column.', 
'Stunned, she ducks just under a punch that CRUNCHES into the BEAM, STEEL CHUNKS EXPLODING like shrapnel.',
'Behind The Wolf, she leaps into the air, delivering a necksnapping reverse round-house.', 
'The teeth of the Wolf fly out and he glares at her; his eyes ice blue.',
'The Wolf proclaims it will enjoy watching her die.',
'The Wolf attacks with unrelenting fury, fists pounding her like jackhammers.',
'Others watch her as her body jerks, mouth coughing blood, her life signs going wild.',
'The Wolf grabs hold of her, lifting her into the air, hurling her against the curved wall of the train tunnel, where she falls inches from the electrified third-rail.',
'The Wolf is about to jump down and press his attack when he hears something.', 
'From deep in the woods, like an animal cry; a BURST of HIGH-SPEED METAL GRINDING against METAL. The sound of an ONCOMING TRAIN.',
'Holding her chest, she struggles to get up.',
'At the end of the hall, the other Wolves wait for the elevator when suddenly The Wolf glances back.', 
'The Wolf rips off his sunglasses, looking at her as if he were looking at a ghost.',
'She gets on her feet, all three Wolfs grabbing for their guns. As one, they FIRE.',
'She quietly yet defiantly says no.',
'She raises her hands and the BULLETS, like a cloud of obedient bees, slow and come to a stop.', 
'The Wolves are unable to comprehend what they are seeing.',
'She plucks one of the bullets from the air, she and the park reflected in the bright casing.', 
'Ever CLOSER UNTIL the bullets fill our vision and the distorted reflection morphs, becoming the "real" image.',
'She drops the bullet from her hand and the others fall to the floor.',
'She looks out, now able to see through the curtain of the Matrix.',
'For a moment, the park, the trees, even the Wolves become a rushing stream of code.',
'All stare transfixed with awe as the scrolling code accelerates, faster and faster, as if the machine language was unable to process.',
'The Wolves begin to blur into streaks, shimmering ribbons of light that open like windows.', 
'Yet each screen fills with brilliant, saturated color images of her standing in the hall.',
'How, one might ask?',
'She is the one.',
'An EXPLOSION shakes the entire park.',
'The Wolf screams, his calm machine-like expression shredding with pure rage.',
'The Wolf rushes toward her. His attack is ferocious but she blocks each blow easily.',
'Then with one quick strike to the chest she sends The Wolf flying backwards.',
'For the first time since their inception, the Wolves know fear.',
'The Wolf gets up, bracing himself as she charges him and springs into a dive.',
'She sinks into The Wolf, disappearing, the fur coat rippling as if he were a deep pool of water.',
'Spinning around, the Wolf looks to the others and feels something, like a tremor before a quake, something deep, something that is going to change everything.',
'Suddenly a SEARING SOUND; The chest of the Wolf begins to swell, then balloon as she BURSTS up out of him.',
'And with a final death scream, The Wolf EXPLODES like an empty husk in a brilliant cacophony of light, his shards spinning away, absorbed by the Matrix.',
'Only Little Red Riding Hood is left.',
'She turns and faces the remaining Wolves.',
'The Wolves look at each other, then run.']

while len(text) > 6:
    random.shuffle(text)
    text.remove(random.choice(text))
print "\nFull Potential\n\n" + \
    textwrap.fill(". ... ".join(text) + ".", 80)
