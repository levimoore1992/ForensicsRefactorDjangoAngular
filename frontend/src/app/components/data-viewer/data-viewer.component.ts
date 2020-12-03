import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {DataService} from "../../services/data.service";
import {Payload} from "../../interfaces/payload";

@Component({
  selector: 'app-data-viewer',
  templateUrl: './data-viewer.component.html',
  styleUrls: ['./data-viewer.component.css']
})
export class DataViewerComponent implements OnInit, OnChanges {

  @Input() view: string = 'presentation';
  @Input() map: boolean = false;
  @Input() filters: [string];
  @Input() data: any;
  @Input() title: string;
  @Input() endpoint: string; //This was called chartName in original application
  @Input() type: string;
  @Input() startDate;
  @Input() endDate;
  loading: boolean = true;




  constructor(private dataService: DataService) {

  }

  ngOnChanges(changes: SimpleChanges): void {

    this.getData()
  }

  ngOnInit(): void {
    if(this.type === undefined){
      throw Error('Dataviewer component needs a type')
    }
    this.getData()
  }

  download() {

  }

  getData(){
    const urlParams = {
      startDate: this.startDate,
      endDate: this.endDate
    };


    this.loading = true;
    this.dataService.getData(this.endpoint, urlParams).subscribe(res => {
      this.data = res;
      this.loading = false
    })
  }
}
