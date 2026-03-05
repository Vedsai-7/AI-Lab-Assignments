# AQI Simple Reflex Agent

This program implements a Simple Reflex Agent that determines the Air Quality Index (AQI) based on pollution data.

## Inputs
Pollution data from a CSV file.

## Sensors
The agent reads environmental data from a file.

## Actuators
Displays the AQI level.

## Rules

PM2.5 <= 50 → Good  
PM2.5 <= 100 → Moderate  
PM2.5 <= 150 → Unhealthy for Sensitive Groups  
PM2.5 <= 200 → Unhealthy  
PM2.5 <= 300 → Very Unhealthy  
PM2.5 > 300 → Hazardous