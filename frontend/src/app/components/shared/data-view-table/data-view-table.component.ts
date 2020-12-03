import {Component, Input, OnInit} from '@angular/core';
import {Payload} from "../../../interfaces/payload";

@Component({
  selector: 'app-data-view-table',
  templateUrl: './data-view-table.component.html',
  styleUrls: ['./data-view-table.component.css']
})
export class DataViewTableComponent implements OnInit {
 @Input() data;
  @Input() displayedColumns;
  columns;

  constructor() {

  }

  ngOnInit(): void {
this.columns = this.displayedColumns.map(col => {
    return col.name
  })
  }

}
