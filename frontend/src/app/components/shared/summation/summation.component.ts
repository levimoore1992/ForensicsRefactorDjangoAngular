import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-summation',
  templateUrl: './summation.component.html',
  styleUrls: ['./summation.component.css']
})
export class SummationComponent implements OnInit {
  @Input() summationData;
  constructor() { }

  ngOnInit(): void {
  }

}
