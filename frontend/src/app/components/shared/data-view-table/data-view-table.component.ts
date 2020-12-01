import {Component, Input, OnInit} from '@angular/core';
import {Payload} from "../../../interfaces/payload";

@Component({
  selector: 'app-data-view-table',
  templateUrl: './data-view-table.component.html',
  styleUrls: ['./data-view-table.component.css']
})
export class DataViewTableComponent implements OnInit {
  @Input() endpoint: string;
  @Input() endpointPayload: Payload //This was called chartName in previous iteration of application
  constructor() { }

  ngOnInit(): void {
  }

}
