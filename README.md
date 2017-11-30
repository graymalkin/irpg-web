# irpg-web

Web interface for the [IdleRPG](http://idlerpg.net/) running
KentIRC. See [here](https://graymalk.in/irc/irpg.html).

## Structure

A python script is run against the IdleRPG database extracting player
information. This is then packaged up into a JSON file and used to
populate the status page.

### Example data

The `data/` directory contains sample data for modifying `status.py`.

 - `irpg.db` is a tab separated table of character and player information
 - `modifiers.txt` is a list of all the fights and player modifications made
   since the beginning of time. E.g. Deity interactions, fights, quests, etc.
 - `questinfo.txt` has information about the current quest in progress
     - I don't know what the fields in this file mean, yet. It might
       be documented in the IdleRPG code.

### Example output
The file is a list of objects, each object represents a user. This is
a truncated verson of the currently live IdleRPG. I only show the
character of `bunu`.


```json
[
	{
		"idled": "8357826",
		"gloves": "29",
		"boots": "61",
		"y_pos": "486",
		"amulet": "40",
		"ring": "48",
		"tunic": "84b",
		"online": "1",
		"level": "56",
		"nick": "bunu",
		"x_pos": "57",
		"on_quest": false,
		"alignment": "g",
		"username": "bunu",
		"class": "King of the Tribbles",
		"weapon": "53",
		"leggings": "35",
		"next_ttl": "176445",
		"helm": "61a",
		"charm": "48",
		"shield": "47"
	}
]
```
