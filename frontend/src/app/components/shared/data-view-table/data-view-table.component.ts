import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-data-view-table',
  templateUrl: './data-view-table.component.html',
  styleUrls: ['./data-view-table.component.css']
})
export class DataViewTableComponent implements OnInit {
  @Input() endpoint: string; //This was called chartName in previous iteration of application
  constructor() { }

  ngOnInit(): void {
  }

}
