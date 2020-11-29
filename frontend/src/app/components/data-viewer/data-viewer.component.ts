import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-data-viewer',
  templateUrl: './data-viewer.component.html',
  styleUrls: ['./data-viewer.component.css']
})
export class DataViewerComponent implements OnInit {

  @Input() view: string = 'presentation';
  @Input() map: boolean = false;
  @Input() filters: [string];
  @Input() data: {map_data: object, stats: object, summation: object, chart: object, chart_layout: object};
  @Input() title: string;
  @Input() endpoint: string; //This was called chartName in original application


  loading: boolean = true;
  linkedStats: boolean;
  stats: boolean;
  chart: boolean;
  summation: boolean;


  constructor() { }

  ngOnInit(): void {
  }

  download() {

  }
}
