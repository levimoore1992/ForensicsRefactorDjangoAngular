import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getData(endpoint, urlParams){
    const params = {};
    if(urlParams.startDate !== undefined && urlParams.endDate !== undefined){
        params['start_date'] = urlParams.startDate;
        params['end_date'] =urlParams.endDate;
    }

    return this.http.get(environment.api + endpoint, {params} )
  }

}
