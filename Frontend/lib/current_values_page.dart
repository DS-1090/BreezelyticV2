import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:redis/redis.dart';

class CurrentData extends StatefulWidget {
  @override
  _CurrentDataState createState() => _CurrentDataState();
}

class _CurrentDataState extends State<CurrentData> {
  String locationValue = 'Hyderabad';
  int pm25Value = 0;

  List<String> locations = ['Hyderabad', 'Delhi'];
  Future<void> fetchDataFromAPI(String location) async {
    final response = await http.get(
      Uri.parse('http://10.0.2.2:8000/sendCurrentAQI?location=$locationValue'),
    );

    if (response.statusCode == 200) {
      print("success!!---------------");
      var data = json.decode(response.body);
      print(data);

      if (data["aqi_data"]?["error"] == 'No data found in Redis') {
        return;
      }

      if (data["aqi_data"]?["status"] == 'ok') {
        setState(() {
          var forecastData = data["aqi_data"]["data"]["forecast"]?["daily"]?["pm25"];
          if (forecastData != null && forecastData.length > 2) {
            print("Real-time AQI: PM2.5 - ${forecastData[2]["avg"]}");
          } 
          else {
            print("Forecast data is missing");
          }

          String fetchedLocation = data["aqi_data"]["data"]["city"]["name"] ??
              "";
          if (fetchedLocation.contains('Hyderabad')) {
            locationValue = 'Hyderabad';
          }

          pm25Value = data["aqi_data"]["data"]["iaqi"]["pm25"]?["v"] ?? "N/A";

          print(locationValue);
          print(pm25Value);
        });
      } else {
        setState(() {
          locationValue = 'Error';
          pm25Value = 0;
        });
      }
    }
  }
    @override
  void initState() {
    super.initState();
    fetchDataFromAPI(locationValue);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Current AQI",
            style: TextStyle(fontSize: 25, fontWeight: FontWeight.w400)),
        centerTitle: true,
        toolbarHeight: 60,
        toolbarOpacity: 0.9,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
            bottomRight: Radius.circular(25),
            bottomLeft: Radius.circular(25),
          ),
        ),
        backgroundColor: Colors.blueAccent[400],
        foregroundColor: Colors.white,
      ),
      body: Center(
        child: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              SizedBox(height: 90),
              Image.asset('assets/logo.png', width: 500, height: 500),
              SizedBox(height: 10),
              Text(
                'Location: $locationValue',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.w400),
              ),
              Text(
                'PM25 Value: $pm25Value',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.w400),
              ),
              SizedBox(height: 20),

            ],
          ),
        ),
      ),
    );
  }
}
