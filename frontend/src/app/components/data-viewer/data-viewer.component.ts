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
  @Input() data: {map_data: object, stats: object, summation: object, chart: object, chart_layout: object};
  @Input() title: string;
  @Input() endpoint: string; //This was called chartName in original application
  @Input() endpointPayload: Payload;

  loading: boolean = true;
  linkedStats: boolean;
  stats: boolean;
  chart: boolean;
  summation: boolean;



  constructor(private dataService: DataService) {}

  ngOnChanges(changes: SimpleChanges): void {
    this.loading = true;
    this.dataService.getData(this.endpoint, this.endpointPayload).subscribe( res => {

      this.loading = false
    })
  }

  ngOnInit(): void {
    this.dataService.getData(this.endpoint, this.endpointPayload).subscribe(res => {
      console.log(res)
      this.loading = false
    })
  }

  download() {

  }
}
