## How is Uber changing Taxis in New York City?

Uber is a new riding model which connects drivers and passengers and provides ride-sharing service with a fair rate.



### Organization of the  project

The project has the following structure:

    DATA515-Project/
      |- data/
     	 |- NYC_Shapes.json
     	 |- NYC_Shapes_Cleaned.json     	 
      |- doc/
         |- Design_Specification_and_Project_Plan.pdf
         |- Functional_Specification.pdf
         |- Presentation_How_is_Uber_Changing_Taxi_in_New_York_City.pdf
         |- Technical_Review
      |- examples/
         |- slider_example
      |- uberTaxi/
         |- test
            |- ...
         |- check_points.py
         |- find_neighborhood.py
         |- geo_convert.py
         |- process_coordinates.py
         |- queries.py
         |- read_json.py
         |- split_data.py
      |- LICENSE
      |- README.md
      |- setup.py
      

### Project Data

* Uber pick-up data

Uber data contains over 18 million Uber pickups in New York City from April to September 2014 and from January to June 2015. FiveThirtyEight originally obtained the data from the NYC Taxi & Limousine Commission (TLC) by submitting a Freedom of Information Law. We downloaded the dataset from Kaggle.com. The uber dataset contain pickup date and time, detailed location information, uber base code. 

* NYC yellow taxi data

The yellow taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The dataset is publicly available: on http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml



### Use Case 
* Uber driver

Uber driver wants to figure out where to find more customers at a specific time of te day. 

* Passanger

Passenger wants to compare the availability of Uber and taxi, and make a decision

* Taxi company 

Taxi company studies their business strategies for the next year.



### Design
* Componets
* Interaction


### Testing


### Limitation and Future Work

