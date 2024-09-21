# It's Fantasy Hockey Time!
## Draft Order Generation

This program is used to generate a random draft order for a fantasy hockey league. 
The order is random except a predetermined subset of players are unable to have a top 3 pick this works as a handicap for players who made the playoffs the previous year.

Running it is very straight forward

`$python draftOrder.py`


It generates a table of percentages which show the percent of the time each players was given each draft pick in a preset large number of simulation.
This is meant to show the adequate randomness of python's random.shuffle() method.

The program then displays what will be considered the 'official' list. The official list is generated after random is seeded with the value 'The Mighty Drunks, Season 5'.
The use of this seed ensures that the 'official' list will always be the same and it is not something that can be regenerated until it provides the output desired by whoever is running it.

Below is the output when run on my machine with 100 million simulations:


    Percentage of the time each player got each draft pick in  100000000  samples
    
    Player		  1st     2nd     3rd     4th     5th     6th     7th     8th     9th     10th
    
	Isaac:		00.00%  00.00%  00.00%  14.29%  14.29%  14.29%  14.28%  14.29%  14.29%  14.28%

	June:		00.00%  00.00%  00.00%  14.29%  14.29%  14.29%  14.29%  14.28%  14.28%  14.29%

	Sam:		16.67%  16.67%  16.67%  07.15%  07.14%  07.14%  07.14%  07.14%  07.14%  07.15%

	Andrew:		00.00%  00.00%  00.00%  14.28%  14.29%  14.28%  14.28%  14.28%  14.29%  14.29%

	London:		00.00%  00.00%  00.00%  14.28%  14.29%  14.29%  14.29%  14.28%  14.29%  14.29%

	Chris D:	16.66%  16.67%  16.67%  07.14%  07.14%  07.14%  07.14%  07.15%  07.14%  07.14%

	Chris R:	16.67%  16.66%  16.67%  07.15%  07.14%  07.14%  07.14%  07.14%  07.14%  07.14%

	Hannah:		16.67%  16.67%  16.67%  07.14%  07.14%  07.14%  07.15%  07.14%  07.14%  07.14%

	Jason:		16.67%  16.67%  16.66%  07.14%  07.14%  07.15%  07.14%  07.15%  07.14%  07.14%

	Shashank:	16.67%  16.67%  16.66%  07.15%  07.14%  07.14%  07.15%  07.14%  07.14%  07.15%   
 
    
    The official order is...
    
    1 )	 Shashank
	
	2 )	 Chris R
	
	3 )	 Hannah
	
	4 )	 Jason
	
	5 )	 Chris D
	
	6 )	 London
	
	7 )	 Isaac
	
	8 )	 June
	
	9 )	 Andrew
	
	10 )	 Sam



**Congratulations Shashank!**
