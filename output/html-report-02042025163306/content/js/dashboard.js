/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.9862258953168044, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "dummy 1"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 10"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 0"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 3"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 2"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 5"], "isController": false}, {"data": [0.9724517906336089, 500, 1500, "Echo"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 4"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 7"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 6"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 9"], "isController": false}, {"data": [1.0, 500, 1500, "dummy 8"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 726, 0, 0.0, 219.0826446280993, 50, 683, 145.0, 439.9000000000002, 482.65, 556.73, 12.120200333889816, 4.330932413397329, 0.7522139764190318], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["dummy 1", 29, 0, 0.0, 297.00000000000006, 70, 483, 326.0, 457.0, 481.5, 483.0, 0.552044468133709, 0.0043128474072946016, 0.0], "isController": false}, {"data": ["dummy 10", 38, 0, 0.0, 298.9736842105264, 73, 494, 299.5, 476.4, 487.34999999999997, 494.0, 0.6771928573974408, 0.005290569198417507, 0.0], "isController": false}, {"data": ["dummy 0", 33, 0, 0.0, 248.84848484848484, 53, 491, 234.0, 475.6, 483.29999999999995, 491.0, 0.635116149271541, 0.004961844916183914, 0.0], "isController": false}, {"data": ["dummy 3", 25, 0, 0.0, 263.84, 50, 481, 250.0, 458.40000000000003, 477.09999999999997, 481.0, 0.4257565694238662, 0.0033262231986239546, 0.0], "isController": false}, {"data": ["dummy 2", 39, 0, 0.0, 278.79487179487177, 51, 496, 240.0, 471.0, 492.0, 496.0, 0.6711755898600856, 0.00524355929578192, 0.0], "isController": false}, {"data": ["dummy 5", 32, 0, 0.0, 296.6875, 67, 493, 304.5, 473.5, 483.24999999999994, 493.0, 0.5751258087706687, 0.004493170381020848, 0.0], "isController": false}, {"data": ["Echo", 363, 0, 0.0, 164.83471074380162, 108, 683, 115.0, 334.8000000000003, 522.2, 632.6000000000001, 6.10114795703985, 4.3126025524396185, 0.7573090607509623], "isController": false}, {"data": ["dummy 4", 38, 0, 0.0, 236.1052631578947, 50, 468, 211.5, 426.5, 449.94999999999993, 468.0, 0.6720192409719521, 0.005250150320093376, 0.0], "isController": false}, {"data": ["dummy 7", 38, 0, 0.0, 281.9473684210526, 57, 499, 288.0, 454.70000000000005, 488.54999999999995, 499.0, 0.6795786612300374, 0.005309208290859667, 0.0], "isController": false}, {"data": ["dummy 6", 31, 0, 0.0, 264.5483870967743, 56, 493, 290.0, 441.20000000000005, 483.4, 493.0, 0.5640465793304221, 0.004406613901018923, 0.0], "isController": false}, {"data": ["dummy 9", 34, 0, 0.0, 274.17647058823525, 68, 495, 299.5, 451.0, 486.75, 495.0, 0.6316180568456251, 0.004934516069106446, 0.0], "isController": false}, {"data": ["dummy 8", 26, 0, 0.0, 263.88461538461536, 64, 500, 231.0, 468.70000000000005, 498.6, 500.0, 0.47031583517238884, 0.0036743424622842883, 0.0], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 726, 0, "", "", "", "", "", "", "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
