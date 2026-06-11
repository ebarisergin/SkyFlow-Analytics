---How many flights were operated?

select COUNT(Flight_ID) as total_flights from fact_flights;


---How many flights were completed, delayed, and cancelled?

select Flight_Status, COUNT(Flight_ID) as flights from fact_flights group by Flight_Status;


---What is the average delay time?

select AVG(Delay_Minutes) as avg_delay_time from fact_delays;


---Which delay category occurs most frequently?

select Delay_Category, COUNT(Delay_ID) as total_delay from fact_delays group by Delay_Category order by total_delay DESC;


---Which airline has the highest average delay?

select a.Airline_Name, AVG(d.Delay_Minutes) as avg_delay from fact_delays d inner join fact_flights f on d.Flight_ID = f.Flight_ID inner join dim_airlines a on f.Airline_ID = a.Airline_ID group by a.Airline_Name order by avg_delay DESC;


---Which route has the highest average delay?

select a1.Airport_Name AS departure_airport, a2.Airport_Name AS arrival_airport, AVG(d.Delay_Minutes) AS avg_delay from fact_flights f inner join fact_delays d on f.Flight_ID = d.Flight_ID inner join dim_airports a1 on f.Departure_Airport_ID = a1.Airport_ID inner join dim_airports a2 on f.Arrival_Airport_ID = a2.Airport_ID group by a1.Airport_Name, a2.Airport_Name order by avg_delay DESC;