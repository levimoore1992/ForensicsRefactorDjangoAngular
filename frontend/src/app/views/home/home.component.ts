import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  tileComponents: {endpoint: string, title: string, strView: string}[] = [
    {endpoint: 'cases_all_by_date',title: 'Cases', strView: 'data'},
    {endpoint: 'service_requests_by_date', title: 'Service Requests', strView: 'data'},
    {endpoint: 'evidence_by_date',title: 'Evidence', strView: 'data'},
    {endpoint: 'backlog_by_unit',title: '(Beta) Backlog By Unit', strView: 'data'},
    {endpoint: 'caseload_by_unit',title: '(Beta) Caseload By Unit', strView: 'data'},
    {endpoint: 'tat_by_unit',title: '(Beta) Turnaround Time By Unit', strView: 'data'},
    {endpoint: 'requests_by_psa',title: '(Beta) Requests By PSA', strView: 'data'},
    {endpoint: 'evidence_types_from_psa',title: '(Beta) Evidence Types From PSA', strView: 'data'},
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
