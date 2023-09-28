# It's Fantasy Hockey Time!
## Draft Order Generation

This program is used to generate a random draft order for a fantasy hockey league. 
The order is random except a predetermined subset of players are unable to have the first overall pick, this works as a handicap for players who made the playoffs the previous year.

Running it is very straight forward

`$python draftOrder.py`


It generates a table of percentages which show the percent of the time each players was given each draft pick in a preset large number of simulation.
This is meant to show the adequate randomness of python's random.shuffle() method.

The program then displays what will be considered the 'official' list. The official list is generated after random is seeded with the value 'The Mighty Drunks, Season 4'.
The use of this seed ensures that the 'official' list will always be the same and it is not something that can be regenerated until it provides the output desired by whoever is running it.

Below is the output when run on my machine with 100 million simulations:


    Percentage of the time each player got each draft pick in  100000000  samples
    
    Player		  1st     2nd     3rd     4th     5th     6th     7th     8th     9th     10th
    
    Isaac:		00.00%  11.12%  11.11%  11.11%  11.12%  11.11%  11.11%  11.11%  11.11%  11.11%
    
    June:		16.67%  09.26%  09.27%  09.26%  09.26%  09.26%  09.26%  09.26%  09.25%  09.25%

    Sam:		00.00%  11.11%  11.11%  11.11%  11.11%  11.12%  11.12%  11.11%  11.11%  11.11%
    
    Andrew:		00.00%  11.11%  11.11%  11.11%  11.11%  11.11%  11.11%  11.12%  11.11%  11.11%
    
    London:		16.66%  09.26%  09.26%  09.26%  09.25%  09.26%  09.26%  09.26%  09.26%  09.26%
    
    Chris D:	16.67%  09.26%  09.26%  09.26%  09.26%  09.26%  09.26%  09.26%  09.26%  09.26%
    
    Chris R:	00.00%  11.12%  11.11%  11.12%  11.11%  11.11%  11.11%  11.11%  11.11%  11.11%
    
    Hannah:		16.67%  09.26%  09.26%  09.26%  09.27%  09.26%  09.26%  09.26%  09.26%  09.26%
    
    Cooper:		16.67%  09.26%  09.26%  09.26%  09.25%  09.26%  09.26%  09.26%  09.26%  09.27%
    
    Shashank:	16.66%  09.26%  09.26%  09.26%  09.25%  09.26%  09.26%  09.26%  09.26%  09.26%
    
    
    The official order is...
    
    1 )	 Hannah
    
    2 )	 Sam
    
    3 )	 London
    
    4 )	 Andrew
    
    5 )	 Cooper
    
    6 )	 Isaac
    
    7 )	 Shashank
    
    8 )	 Chris R
    
    9 )	 Chris D
    
    10 )	 June
    


**Congratulations Hannah!**
