import { Component, OnInit } from '@angular/core';
import {Payload} from "../../interfaces/payload";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  tileComponents: {endpoint: string, title: string, strView: string, cols: number, rows: number}[] = [
    {endpoint: 'cases_all_by_date',title: 'Cases', strView: 'data', cols: 1, rows:1},
    {endpoint: 'service_requests_by_date', title: 'Service Requests', strView: 'data', cols:1, rows:1},
    {endpoint: 'evidence_by_date',title: 'Evidence', strView: 'data', cols:1, rows: 1},
    {endpoint: 'backlog_by_unit',title: '(Beta) Backlog By Unit', strView: 'data', cols:3, rows:2},
    {endpoint: 'caseload_by_unit',title: '(Beta) Caseload By Unit', strView: 'data', cols:3, rows:2},
    {endpoint: 'tat_by_unit',title: '(Beta) Turnaround Time By Unit', strView: 'data', cols:3, rows: 2},
    {endpoint: 'requests_by_psa',title: '(Beta) Requests By PSA', strView: 'data', cols:3, rows:2},
    {endpoint: 'evidence_types_from_psa',title: '(Beta) Evidence Types From PSA', strView: 'data', cols:3, rows:2},
  ];
  startDate: Date;
  endDate: Date;
  endpointPayload: Payload;
  constructor() { }

  ngOnInit(): void {
    this.endpointPayload = {
      startDate: this.startDate,
      endDate: this.endDate
    }
  }

  changeStartDate(event) {
    this.endpointPayload.startDate = event
  }

  changeEndDate(event){
    this.endpointPayload.endDate = event
  }
}
