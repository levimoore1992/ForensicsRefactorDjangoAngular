import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  tileComponents: {endpoint: string, title: string, strView: string, cols: number, rows: number}[] = [
    {endpoint: 'backlog_by_unit',title: '(Beta) Backlog By Unit', strView: 'data', cols:3, rows:2},
    {endpoint: 'caseload_by_unit',title: '(Beta) Caseload By Unit', strView: 'data', cols:3, rows:2},
    {endpoint: 'tat_by_unit',title: '(Beta) Turnaround Time By Unit', strView: 'data', cols:3, rows: 2},
    {endpoint: 'requests_by_psa',title: '(Beta) Requests By PSA', strView: 'data', cols:3, rows:2},
    {endpoint: 'evidence_types_from_psa',title: '(Beta) Evidence Types From PSA', strView: 'data', cols:3, rows:2},
  ];
  startDate: string;
  endDate: string;
  constructor() { }

  ngOnInit(): void {

  }

  changeStartDate(event) {
    this.startDate = event
  }

  changeEndDate(event){
    this.endDate = event
  }
}
