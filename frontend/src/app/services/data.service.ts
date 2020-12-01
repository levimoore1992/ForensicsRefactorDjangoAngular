import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getData(endpoint, payload){
    const httpParams = new HttpParams();

    payload.hasOwnProperty('startDate') ? httpParams.set('start_date', payload.startDate): null;
    payload.hasOwnProperty('endDate') ? httpParams.set('end_date', payload.endDate): null;

    return this.http.get(environment.api + endpoint, {params: httpParams} )
  }

}
