import {Component, Input, OnInit} from '@angular/core';
import {Payload} from "../../../interfaces/payload";

@Component({
  selector: 'app-data-view-table',
  templateUrl: './data-view-table.component.html',
  styleUrls: ['./data-view-table.component.css']
})
export class DataViewTableComponent implements OnInit {
 @Input() data;
  displayedColumns = ['case_id', 'close_date'];
  constructor() { }

  ngOnInit(): void {

  }

}
