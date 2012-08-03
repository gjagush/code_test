# Copyright (c) 2012, Gabriel Allen Jagush
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list 
# of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice, this 
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT 
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from sys import exit

global key_inv
key_inv = False

global poker_inv
poker_inv = False

global trap_ent

global rope_inv
rope_inv = False

global hall_block
hall_block = False

global unlocked
unlocked = False

global amulet_inv
amulet_inv = False

global gun_inv
gun_inv = False

global first_entrance
first_entrance = True

global crossed
crossed = False

global chasm_ent

global freedom
freedom = False

global cthulhu_inv
cthulhu_inv = False

def introduction():
    print """
The night is closing in on you, and the rain is pouding on the roof of your
automobile. You had made your trip in the early morning and had spent all day
researching the history of lost civilizations and their heathen gods to try
and gleam some insight in to recent killings in the area that are being
attributed to a cult of immigrants from the Pacific.

On your way back, however, you found that the road you used to get to the
city is now washed out, which is why you are now driving on this God-forsaken
back road. You are not sure if you have enough gasoline.

The engine sputters and dies. Your fears seem to not be unfounded. In the 
distance, however, lights shine from a house on a hill. Staring at the car,
you realize that there is no way that you are going to make it to your home
before the next break of dawn. Your best bet from weathering the night and 
hiding from the storm is to hide in the house. If the residents are there, 
they may be able to provide you with enough fuel to get home in the morning.

You start your long trek up the hill. With each step you take, the lights
of the house become harder and harder to see. It's almost as if they are 
getting dimmer as you get closer. At the entrance to the grounds, a large
gate annouces "Darzmoor Manor." At one point in time, a heavy chain held this
gate shut, but the chain now lies in the mud, a rusted fragment of what it 
used to be. Pushing the gate further open, you press forwards.

A scream rockets out of the building and you leap forwards. It sounds like
the cry of a young woman. Bouding towards the door, you reach it in a haste,
and trying to stop yourself, you slip in the mud. Pain sears through your 
leg. Lifting up your leg, you see that you've gashed open the side of your
calf. You stand up, and realize that you injured your ankle and have to limp
severely when you are walking.

Straining, you latch yourself to the doorframe, and pound on the door. If
you didn't need help before, you certainly need it mow.

The door to the manor swings open in silence. There is no maid, no welcoming
butler, nobody to greet you.

You stare into the blackness past the door. A feeling of dread seeps through
you, and it feels like the darkness is looking back at you, glaring. However,
someone in the manor clearly called for help, and you need medical attention.

Dare you enter the manor?
"""
    while True:
        user = raw_input("> ")
        if "yes" in user or user == "y":
            print """
You charge into the darkness as fast as you are able with your injured leg.
You are a brave soul indeed, but do not let your bravery take your life.
"""
            entrance()
        elif "no" in user or user == "n":
            print """
There can be wisdom in cowardice.
"""
            exit()
            
def entrance():
    global key_inv
    global trap_ent
    global first_entrance

    if first_entrance == True:
        print """
As you step through the threshold of the manor, the wind howls and blows. 
The door slams shut behind you, trapping you in a dimly-lit room. You find 
yourself standing in the entrance of Darzmoor Manor. The ceiling lofts high 
above your head, retreating into the darkness. Coat racks surround you, 
covered in rich furs and hats that your father might have worn when he was 
a young man. Mirrors stand along the walls in order for visitors to adjust 
themselves before entering the main house, and an umbrella stand made of an 
elephant's foot sits by a small table. 

There are doors to the west, north, and east.
"""
        first_entrance = False
    elif first_entrance == False and freedom == False:
        print """
The ceiling of the manor entrance hall lofts high above your head, retreating 
into the darkness. Coat racks surround you, covered in rich furs and hats 
that your father might have worn when he was a young man. Mirrors stand along 
the walls in order for visitors to adjust themselves before entering the main 
house, and an umbrella stand made of an elephant's foot sits by a small table. 

There are doors to the west, north, and east.
"""
    else:
        print """
You are once again standing in the entrance hall to Darzmoor Manor. This time,
however, the main door to the south is open, ready for you to escape.
""" 
    while True:
        user = raw_input("> ")
        if ("look" in user or "table" in user) and key_inv == False:
            print """
A basket for calling cards has been placed on the table. It contains only
one card, belonging to someone by the name of Lord James Greenwald. A 
skeleton key lays next to the basket, buried under dust."""
        elif ("look" in user or "table" in user) and key_inv == True:
            print """
A basket for calling cards has been placed on the table. It contains only 
one card, belonging to someone by the name of Lord James Greenwald."""
        elif "west" in user or user == "w":
            roperoom()
        elif "east" in user or user == "e":
            trap_ent = "west"
            traproom()
        elif "north" in user or user == "n":
            altar()
        elif "key" in user and key_inv == False:
            print """
You take the key, dust it off, and put it in your pocket.
"""
            key_inv = True
        elif ("leave" in user or "south" in user or user == "s") and freedom == True:
            ending()
        else:
            print """
I don't understand.
"""

def traproom():
    global trap_ent
    print """
This room is sparse and seems to have taken the brunt of Time's attack.
There is a painting of some hideous creature on the eastern wall, and 
the southern wall allows some light in through a tiny window near the
ceiling. There are doors to the west and to the north.
"""
    while True:
        user = raw_input("> ")
        if user == "look":
            print """
The painting is of a huge beast, towering over the ocean as it emerges
from the depths. Grayish green and scaled, it would bear a reptillian
resemblance if not for the wings on its back, its humanoid limbs, and, 
worst of all, the tentacles covering its face. The painting fills you
with horror.

The floorboards are severely rotten.
"""
        elif ("north" in user or user == "n"):
            if trap_ent == "west":
                print """
As you cross the room, you hear the floorboards creaking in protest.
The mold and the rot has gotten to the floor, and it collapses under you,
sending you flying into a dark hole. You strike your head, and the last
thing that passes through your mind is the image of the creature in the 
painting, reaching for your throat. You breathe your last, and you die 
alone, and in the dark.
"""
                exit()
            else:
                pokerroom()
        elif("west" in user or user == "w"):
            if trap_ent == "north":
                print """
As you cross the room, you hear the floorboards creaking in protest.
The mold and the rot has gotten to the floor, and it collapses under you,
sending you flying into a dark hole. You strike your head, and the last
thing that passes through your mind is the image of the creature in the 
painting, reaching for your throat. You breathe your last, and you die 
alone, and in the dark.
"""
                exit()
            else:
                entrance()
        else:
            print """
I don't understand
"""

def altar():
    global key_inv
    global unlocked
    global amulet_inv
    print """
This may, at one point, have been a dining room. It no longer appears
that way. The grand table in the centre of the room has be decorated with
ritual candles and skulls, some animal, some perhaps human. The room 
stinks of pungent incense and of iron. Animal pelts have been used to
line the walls, and a great many of them have been torn down to cover
the surface of the table. There are doors to the south and to the east.
"""
    while True:
        user = raw_input("> ")
        if user == "look" and unlocked == False:
            print """
Settled within the pile of furs in the centre of the table lies a small
box, locked tightly. The box is made of metal and engraved with many tiny
carvings of geometric shapes that cannot exist in the physical world.
"""
        elif user == "look" and unlocked == True:
            print """
In the middle of the mountain of furs on the tables lies an unlocked box.
"""
        elif ("unlock" in user or "key" in user) and key_inv == True and unlocked == False:
            print """
You unlock the little box with the skeleton key, and lift up the lid.
The opened box reveals an amulet of bright blue stones, precious and
transparent enough to look through.The end of the amulet ends in a 
curious seal, carved of jade. You place the amulet around your neck.
"""
            unlocked = True
            amulet_inv = True

        elif ("unlock" in user or "key" in user) and key_inv == False:
            print """
You need a key for that!
"""
        elif ("unlock" in user or "key" in user) and key_inv == True and unlocked == True:
            print """
You've already unlocked that.
"""
        elif "east" in user or user == "e":
            pokerroom()
        elif "south" in user or user == "s":
            entrance()
        else:
            print """
I don't understand.
"""
            

def pokerroom():
    global poker_inv
    global trap_ent
    global hall_block
    print """
The walls of this room are lined with bookshelves. The books are packed
in so densely that the room could be missing its walls, and you would
never notice. Ancient and dusty, you fear bumping into these books that 
all look like they might disintegrate on touch. Strange paintings hang 
high above the book cases and framed sketches of dream-like monstrosities
are hung on the ends of the bookshelves that have been placed in the
middle of the room. There are doors to the south and to the west.
"""
    while True:
        user = raw_input("> ")
        if "south" in user or user == "s":
            trap_ent = "north"
            traproom()
        elif "west" in user or user == "w":
            altar()
        elif "look" in user:
            print """
A mountain of rubble at the northern end of the room looks like it may
have been a fireplace many years ago. Through the rubble, you can see an
odd glow emanating from the deep. By the fireplace lies an overturned stand
with an iron fireplace poker in it.
"""
        elif ("take" in user or "poker" in user) and poker_inv == False and hall_block == False:
            print """
You take the poker from the stand. It has a solid weight, and while rusty,
has withstood the tests of time well.
"""
            poker_inv = True
        elif "read" in user:
            print """
The books are mostly in Arabic, Latin, and Greek, although there are some
languages whose alphabets you do not recognize. Many of the books deal
with the stars, and some discuss ancient gods whose mythology you have
been unfamiliar with. The illustrations are similar to the sketches in the
library and they make your stomach turn.
"""
        else:
            print """
I don't understand.
"""

def roperoom():
    global rope_inv
    global crossed
    print """
A thick Persian carpet splays over the floor of this room. Your best guess
is that this room was used to entertain guests, most likely as a smoking
room. The old smoke has permeated the furniture of the room, a deep burgundy
set of corderoy armchairs and a couch. A small personal bar showcases a 
multitude of old bottles, all either cracked or empty. Tobacco pipes of 
various shapes and sizes litter a table by one of the armchairs. There are
doors to the north and to the east.
"""
    while True:
        user = raw_input("> ")
        if "north" in user or user == "n":
            crush_hall()
        elif "east" in user or user == "e":
            entrance()
        elif "look" in user:
            print """
One corner of the carpet is turned up and bunched, revealing a long portion
of rope. The rope may have been used as part of a servant's pullcord system.
"""
        elif ("take" in user or "rope" in user) and rope_inv == False and crossed == False:
            print """
You take the rope.
"""
            rope_inv = True
        else:
            print """
I don't understand.
"""

def crush_hall():
    global poker_inv
    global hall_block

    if hall_block == True:
        print """
You walk back into the deadly hallway. Its progress has been halted by the
poker you obtained, which is jammed between the walls as a brace. The poker
is lodged fast from the pressure of the walls closing in, but there is a
distinct bow in the poker's length. You don't know how much longer the poker
will be able to keep the walls apart. There are doors to the north and south.
"""
    else:
        print """
You walk into a long hallway decorated sparsely, with no side tables nor wall
hangings adorning it. A long black smear on the wood floor hints at something
gruesome having transpired long ago. When you have reached the middle of the
hallway, you realized the walls have been moving slowly together the entire
time, and are now closing together quite rapidly. Freedom lies to the south and
to the north, but if you do not act quickly, you will find death.
"""

    while True:
        user = raw_input("> ")
        if ("north" in user or user == "n") and hall_block == True:
            gunroom()
        elif ("south" in user or user == "s") and hall_block == True:
            roperoom()
        elif ("north" in user or "south" in user or user == "n" or user == "s") and hall_block == False:
            print """
You leap from the exit, dashing madly forwards, but the walls move faster and
faster, encountering no resistance. You almost make it to safety. Almost. The
walls slam together, crushing your body to an unrecognizable pulp. The last 
thought that you had before the walls obliterated your skull was that you wouldn't
have had time to open the door, anyway.
"""
            exit()
        elif user == "look":
            print """
Glancing quickly, you see that the walls are closing in together down the length
of the hallway. You may be able to keep the walls forced apart somehow.
"""
        elif ("poker" or "prop" in user) and poker_inv == True:
            print """
You hold the poker out horizontally in front of you, perpendicular to the walls.
The walls slam into the poker. It bends slighly, almost traitorously, but it
holds, and you are safe. For now.
"""
            hall_block = True
        else:
            print """
I don't understand.
"""

def gunroom():
    global gun_inv
    global chasm_ent
    print """
The stench of decay hangs in the air of this room. The first thing that you see
on entering this room is a body lying in the far corner of the room. It, like
everything else in this house, is covered with a thick layer of dust. This fellow
has been here for a while. There is some minor amount of disarray near the body,
but otherwise the room is fairly tidy. A desk and a few bookcases indicate that it
was formerly employed as an office for personal or perhaps minor business matters.
There are doors to the east and to the south.
"""
    while True:
        user = raw_input("> ")
        if "east" in user or user == "e":
            chasm_ent = "west"
            chasm()
        elif "south" in user or user =="s":
            crush_hall()
        elif ("look" in user or "corpse" in user or "body" in user) and gun_inv == False:
            print """
Nothing catches your attention more than the body on the floor. Examining it, you
see that this man was a formerly a private eye from Arkham. Any identification 
papers are long gone and dissolved, but his badge, dusty and worn survives. A 
government-issued Springfield Armory Model 1911 is holstered at his side, a proud 
example of American firepower.
"""
        elif ("look" in user or "corpse" in user or "body" in user) and gun_inv == True:
            print """
Nothing catches your attention more than the body on the floor. Examining it, you
see that this man was a formerly a private eye from Arkham. Any identification 
papers are long gone and dissolved, but his badge, dusty and worn survives.
"""
        elif ("gun" in user or "take gun" in user or "handgun" in user) and gun_inv == False:
            print """
You take the gun and check to see if it is loaded. Seeing that the gun is live and
ready for action, you take the holster off of the dead man and strap it onto yourself.
THe heavy gun bears its full weight on you, but its presence is a comfort in this
nightmarish manor.
"""
            gun_inv = True
        else:
            print """
I don't understand.
"""

def chasm():
    global rope_inv
    global crossed
    global chasm_ent
    print """
A great hole has obliterated the middle of this room. The hole reaches so far down 
that the extents of its depths are obscured by darkness. You try to wrap your mind
around the sheer size of the pit, but there are few explanations that come to mind.
The best reason for the hole's existance that you can think of is that a sinkhole must
have formed under the foundation of the old house and taken this room with it when
it finally collapsed.

There are four statues in this room, a pair each flanking the doors on the eastern
wall and on the western wall. The statues depict obscene creatures with too many eyes
and too many limbs. The shortest statue is five feet tall, and the largest statue
is about nine feet tall, standing two men abreast.
"""
    while True:
        user = raw_input("> ")
        if "east" in user or user == "e":
            if crossed == True:
                cthulhu()
            else:
                print """
Your path is blocked by the pit."""
        elif "west" in user or user == "w":
            gunroom()
        elif "cross" in user and crossed == True:
            if chasm_ent == "east":
                gunroom()
            elif chasm_ent == "west":
                cthulhu()
        elif rope_inv == True and "rope" in user:
            print """
You tie the end of the rope into a loop and toss it across the pit. It hooks onto
a vile-looking horn adorning one of the hideous statues and holds. You tie the other
end around one of the statues next to you. The rope spans the chasm like a bridge 
built by savage Amazonian warriors.
"""
            crossed = True
        elif "jump" in user or "leap" in user:
            if gun_inv == False:
                print """
You attempt to cross the pit through a feat of pure athleticism, taking a running
start, and leaping once you hit the end. Unfortunately, your hurt ankle proves to be
too severe of an injury, and you are not able to launch yourself with enough force. 
You fall through the blackness, air rushing past your face, but you don't hit the ground. 
Instead, you just feel the sensation of falling and you see the entrance of the pit fading 
further and further away. An eternity passes, and your mind follows. You dream of naught 
but dark planes of existance, and when you wake, your senses are useless. You hunger 
and thirst, but do not die. The void embraces your existance.

Permanently.
"""
                exit()
            else:
                print """
You attempt to cross the pit through a feat of pure athleticism, taking a running
start, and leaping once you hit the end. Unfortunately, your hurt ankle proves to be
too severe of an injury, and you are not able to launch yourself with enough force. 
You fall through the blackness, air rushing past your face, but you don't hit the ground. 
Instead, you just feel the sensation of falling and you see the entrance of the pit fading
further and further away. Days seem to pass, and you become hungrier and more desperate.
Realizing that this is a permanent predicament, you struggle to reach the pistol holstered 
at your side. With some effort, you move your arm against the rushing air and put the 
barrel in your mouth. Death is now only a sweet release from an enternity of falling and 
starvation. You pull the trigger and life goes blank.
"""
                exit()
        else:
            print """
I don't understand.
"""

def cthulhu():
    global amulet_inv
    global chasm_ent
    global gun_inv
    global cthulhu_inv
    global freedom
    print """
A long set of stairs lead down, down, down into the earth, explaining why the pit you
saw was so deep. You pass by tunnel after tunnel, all blocked by stones brought down
by collapses. Time has been making short work of this underground network, leaving only
the main tunnel, which is larger and highly reinforced. You reach a set of massive double
doors covered in ancient carvings of monsters and beasts beyond the imagination. The
doors were forced open a long time ago, and it looks like the carvings have been ruined
by large claw marks.

Past the doors, there is a central chamber, much like a temple. The walls and floor are
made completely of black marble, and the supporting columns all around the edge of the
room are a bloody red. An altar made of white granite stands in the centre of the room.
The walls are lined with gruesome statues much like the ones you saw before, but these
are made of some sort of crystal that glows a dark red.
"""
    while True:
        user = raw_input("> ")
        if "west" in user or user == "w":
            chasm_ent = "east"
            chasm()
        elif "look" in user:
            print """
You walk around the room and look at each of the statues. You have never seen anything
like these statues, these carved monstrosities that cast an ugly pallor on your skin
with their otherwordly glow, and curves that defy the laws of geometry. Mustering the 
courage to go up to the central altar, you see that on a small pedestal in the middle 
of the altar sits a much smaller statue. It has a large, bulbous head, draconic wings,
tentacles protruding from its face, and long devil claws. Its body is made of a dark
jade, and its eyes have been formed by rubies.
"""
        elif ("take" in user or "statue" in user or "idol" in user or "statuette" in user or "Cthulhu" in user) and cthulhu_inv == False:
            if amulet_inv == False:
                if gun_inv == True:
                    print """
As you grab the idol, you are stricken with blinding pain. Screaming, you writhe on
the floor in agony as your vision fades to black. You feel your skin being shredded off
by thousands of invisible rats and your joints begin to melt. In your writhing fit, your
gun accidentally goes off. As you bleed out, you stare at your gun and wonder how it could
have gone off accidentally while it was sitting so comfortably in your hand.
"""
                    exit()
                else:
                    print """
As you grab the amulet, you are stricken with blinding pain. Screaming, you writhe on
the floor in agony as your vision fades to black. You feel your skin being shredded off
by thousands of invisible rats and your joints begin to melt. You lay on the floor, 
now immobile, mouth open in a silent scream. The pain transcends all sensation and you
feel yourself drifting apart, molecule by molecule, atom by atom. Soon there is nothing
left of you, and your particles have dissapated into the atmosphere, rising through the
microscopic cracks in rock and earth until they have reached the sky.Your consciousness
remains intact, but now only as a formless creature, blowing around in the solar winds.
"""
                    exit()
            else:
                print """
You put the idol in your pocket and feel slower, heavier. The amulet around your neck 
glows bright and fierce. A warmth emanates from it, comforting you. A wind, deep from
the tunnels, blasts through the chamber, and your surroundings seem much brighter.
"""
                freedom = True
        else:
            print """
I don't understand.
"""

def ending():
    print """
Although you thought this moment was never going to arrive, you are finally leaving 
the cursed hive of wretchedness that is Darzmoor Manor. Time seems to have passed much 
faster than you thought, as daylight has arrived. You walk down the hill of the property,
wading through the tall grass, struggling more than you did coming up the hill at first.

When you get to the road, you look for your car. At first you don't recognize it, but it
dawns on you that the rusty heap of metal parts by the side of the road is actually a car.
Searching it, you find dust and fragments of fabric, but on the floor under the driver's
seat, you find an old penknife. Opening the rusty blade with force, you see your initals
boldly engraved on the side of the knife. In shock, you stare back at the hill.

Save for the ruins of a long-forgotten chimney, there is nothing left of Darzmoor Manor.
"""
    exit()

introduction()
