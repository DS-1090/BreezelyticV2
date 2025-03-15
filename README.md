# BreezelyticV2


## Overview
BreezelyticsV2 provides real-time air quality data by displaying current PM2.5 values for a given location. 

It also offers historical records and future predictions of air pollution levels and graphical representation of that data. 

The system is designed with a scalable architecture utilizing various modern technologies for data processing and storage.

I have extensively documented my learnings as well.

This project is also an exploration of big data handling technologies.

### Key Features:
- **Real-time PM2.5 Data**: Retrieves air quality information from the API of `https://aqicn.org/`.
- **Historical & Forecast Data**: Stores past records and  future values.
- **Docker Compose Network**: Orchestrates Django, Spark, Redis and Kafka services efficiently.
- **Scalable Architecture**: Supports large-scale data processing with Spark and Redis.

## Tech Stack
- **Backend**: Django (API communication, middleware and Frontend interaction)
- **Frontend**: Flutter (Mobile application for UI/UX)
- **Processing Engine**: Apache Spark (Data processing)
- **Database**: Redis (In-memory storage for quick access)
- **Streaming**: Apache Kafka (Real-time data pipeline)
- **Containerization**: Docker (Encapsulation and portability of services)

## Workflow
The system operates as follows:
1. Django fetches real-time data from `https://aqicn.org/` and sends it to Kafka Producer.
2. The Kafka Consumer stores the data in Redis for quick access.
3. The **mobile app (Flutter)** requests PM2.5 data current data from the **Redis**.
4. Django fetches records data from `https://aqicn.org/` and stores it as a CSV file.
5. **Apache Spark** processes and retrieves records from CSV .
6. The data is then sent back to the mobile app for display of records.
7. All services communicate within the **Docker Compose Network** (`airnet`).

Flow:

![Screenshot 2025-03-15 185010](https://github.com/user-attachments/assets/76dd352a-77f1-4441-a3f5-01efc968e99d)

## Setup & Installation
### Prerequisites
Ensure you have the following installed on your system:
- Docker
- Python & Django
- Flutter SDK
- Apache Spark
- Apache Kafka
- Redis
### Steps to Run the App
1. **Clone the repository:**
   ```bash
   git clone https://github.com/DS-1090/BreezelyticV2
   cd Backend
   ```
   
2. **Build Django App Image:**
   ```bash
   docker build -t djangoapp .
   ```
3. **Build Kafka Consumer Image:**
   ```bash
   docker build -t kafka-consumer .
    ```
4. **Set up and run Docker containers and create Docker Compose Network:**
   ```bash
   docker-compose up --build
   ```

5. **Run the Flutter App:**
   ```bash
   cd frontend
   flutter run
   ```

## Future Improvements
- **MySQL Integration**: Implement RelationalDB for storing records
- **Enhanced Spark Processing**: Expand data processing capabilities using Spark 

## Spark Web
![Screenshot 2025-03-04 175130](https://github.com/user-attachments/assets/f9d3337c-5c9a-401a-bfd3-793806dbf45f)


## Redis DataBase
![Screenshot 2025-03-15 001217](https://github.com/user-attachments/assets/6f90260e-bb9e-4777-bf42-6ffa22addc9a)

## Kafka
![Screenshot 2025-03-15 001250](https://github.com/user-attachments/assets/8fa43aec-d54a-4604-80e3-b0c0c7194317)



## Mobile App


- **Current Location PM2.5 Data**
  
![Screenshot 2025-03-15 001024](https://github.com/user-attachments/assets/7187d9df-179a-4c60-978e-5a996073d69e)


- **Home Screen**
  
![Screenshot 2025-03-15 000234](https://github.com/user-attachments/assets/25f2198e-62a4-4084-bbf7-6d2a3d33d82c)


- **Records Page**
  
![Screenshot 2025-03-15 000203](https://github.com/user-attachments/assets/d62dd4b4-3af9-418e-be70-192cb89126ec)


- **Graph Page**
  
  ![Screenshot 2025-03-15 000220](https://github.com/user-attachments/assets/c413a214-d2fe-4c93-ace6-ce92c30fccf0)

- **Loading Screen**
  
  ![image](https://github.com/user-attachments/assets/dec38bba-5ead-4320-af1c-08063d3b99a6)

