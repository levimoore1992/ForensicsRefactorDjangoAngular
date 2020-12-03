import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-chart',
  template: '<plotly-plot [data]="chartData.data" [layout]="chartData.layout"></plotly-plot>',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {
  @Input() chartData;
  layout = {};
  constructor() { }

  ngOnInit(): void {

    this.chartData = {
        data: [
            { x: [1, 2, 3], y: [2, 6, 3], type: 'scatter', mode: 'lines+points', marker: {color: 'red'} },
            { x: [1, 2, 3], y: [2, 5, 3], type: 'bar' },
        ],
        layout: {width: 320, height: 240, title: 'A Fancy Plot'}
    };
  }

}
