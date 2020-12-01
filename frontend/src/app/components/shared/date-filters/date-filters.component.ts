import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatDatepickerInputEvent} from "@angular/material/datepicker";

@Component({
  selector: 'app-date-filters',
  templateUrl: './date-filters.component.html',
  styleUrls: ['./date-filters.component.css']
})
export class DateFiltersComponent implements OnInit {
  @Output() startDateChange: EventEmitter<Date> = new EventEmitter;
  @Output() endDateChange: EventEmitter<Date> = new EventEmitter;
  selected: string = 'custom';

  constructor() { }

  ngOnInit(): void {
  }

  changeDate(type:string , event: MatDatepickerInputEvent<Date>) {

    switch (type){
      case 'start':
        this.startDateChange.emit(event.value);
        break;

      case 'end':
          this.endDateChange.emit(event.value);
        break
    }


  }
}
