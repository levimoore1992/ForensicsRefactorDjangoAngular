import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-chart',
  template: '<plotly-plot [data]="chartData.data" [layout]="layout"></plotly-plot>',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {
  @Input() chartData;
  layout = {width: 700, height: 400, type:'scatter', xaxis: {type: 'date'}};
  constructor() { }

  ngOnInit(): void {

  }

}
