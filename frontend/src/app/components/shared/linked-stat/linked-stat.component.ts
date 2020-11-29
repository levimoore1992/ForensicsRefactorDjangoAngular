import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-linked-stat',
  templateUrl: './linked-stat.component.html',
  styleUrls: ['./linked-stat.component.css']
})
export class LinkedStatComponent implements OnInit {
  @Input() stats;
  constructor() { }

  ngOnInit(): void {
  }

}
