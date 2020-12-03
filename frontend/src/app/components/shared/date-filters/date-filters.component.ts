import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatDatepickerInputEvent} from "@angular/material/datepicker";

@Component({
  selector: 'app-date-filters',
  templateUrl: './date-filters.component.html',
  styleUrls: ['./date-filters.component.css']
})
export class DateFiltersComponent implements OnInit {
  @Output() startDateChange: EventEmitter<string> = new EventEmitter;
  @Output() endDateChange: EventEmitter<string> = new EventEmitter;
  selected: string = 'custom';

  constructor() { }

  ngOnInit(): void {
  }

  changeDate(type:string , event: MatDatepickerInputEvent<Date>) {

    switch (type){
      case 'start':
        let st = this.convertDate(event.value);
        this.startDateChange.emit(st);
        break;

      case 'end':
          let ed = this.convertDate(event.value);

          this.endDateChange.emit(ed);
        break
    }


  }

  convertDate(value: Date): string {

    return (value.getMonth() + 1) +
    "/" +  value.getDate() +
    "/" +  value.getFullYear();
  }
}
