This file provides users detailed examples of how to use our interface and what they can do with the interface.
## Getting Started
Our interface mainly consists of two parts: regional heat map and filter options.
### Regional Heat Map
Regional heat map summarizes and aggregates data within pre-defined hundreds of neighborhoods in New York City. Initially, it displays community district boundaries and color of this neighborhood generates by corresponding number of pickups. Without making any selections, users can have a general overview of what kind of information they can have from heat map by simply hover over it. When a user hovers over a neighborhood, it displays a popup containing neighborhood name, number of pickups in this neighborhood and geographic coordinates of current point.
![ss1](https://cloud.githubusercontent.com/assets/26759376/26755754/57157ce2-4849-11e7-84cb-8e4a1bdf61be.png)

### Filter Options
The filter options allow users to select between Uber and taxi as well as a certain period they feel they are most interested in. Fliters include a checkbox button group, a slider and two dropdown menus. Checkbox button group provides selections between Uber and taxi. The initial value is Uber data on April 1st at hour 0. Users can select either some of the fliters or all of the fliters. If only some of fliters are selected, then the others will keep their initializing defaults.


## Examples
### Case 1
Assume one of our users is an uber driver. As a part-time uber driver, he only spends three hour to drive uber per day. He lives in ridgewood and he wants to find which hours has most pickups in his neighborhood by using our interface. In order to have pickups as many as possible, he wants to figure out when is the best time to start his driving during a day. 

The user only needs to check uber data in this case. I suggest him random selects several days during each month and moves the hour slider side to side. By looking at changes in the color and the number of pickups in his neiborhood, he'll find which hours of a day normally have most pickups around his place. The results will give him a suggestion on his start time.

### Case 2
Suppose a user plans to visit NYC next month (July), he booked a hotel in ....... district. He would like to go to nightclubs at midnight. He feels it is kind of hard to request a ride at such a late night, so he wants to use our interface to check whether request a taxi or uber ride is better for him at his location.

For his case, I suggest him switches between uber and taxi and compare the number of pickups at midnight at his location for several days in July. He can either tell from the change of color or the number shown in popup. He can also do the same step but select other months to help him make a better decision.

### Case 3
Our users can also be some taxicab companies. A taxicab company had 200 taxicabs last year. However, only 80% taxicabs were rented out. The company wants to figure out what are possible reasons behind the case. The company wants to use our interface to 

