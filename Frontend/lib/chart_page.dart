import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:breezelyticsv2/records_page.dart';

class ChartPage extends StatefulWidget {
  final List<Map<String, dynamic>> records;

  const ChartPage({super.key, required this.records});

  @override
  State<ChartPage> createState() => _ChartPageState();
}

class _ChartPageState extends State<ChartPage> {
  @override
  Widget build(BuildContext context) {
    List<Map<String, dynamic>> records = widget.records;

    return Scaffold(
      appBar: AppBar(title: const Text("AQI Graph",
          style: TextStyle(fontSize: 25, fontWeight: FontWeight.w400)),
        centerTitle: true,
        toolbarHeight: 60,
        toolbarOpacity: 0.9,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
              bottomRight: Radius.circular(25),
              bottomLeft: Radius.circular(25)
          ),
        ),
        backgroundColor: Colors.blueAccent[400],
        foregroundColor: Colors.white,
      ),
      body: Container(
        height: 300, 
        padding: const EdgeInsets.all(8.0),
        child: SfCartesianChart(
          primaryXAxis: CategoryAxis(), 
          series: <CartesianSeries>[
            LineSeries<Map<String, dynamic>, String>(
              dataSource: records,
              xValueMapper: (record, _) => record['date'],
              yValueMapper: (record, _) => record['avg_pm25'],
            )
          ],
        ),
      ),
    );
  }
}
