import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DataViewerComponent } from './components/data-viewer/data-viewer.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HomeComponent } from './views/home/home.component';
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatListModule} from "@angular/material/list";
import {HttpClientModule} from "@angular/common/http";
import {MatCardModule} from "@angular/material/card";
import { InputFilterComponent } from './components/filters/input-filter/input-filter.component';
import { MultiSelectFilterComponent } from './components/filters/multi-select-filter/multi-select-filter.component';
import { DateFilterComponent } from './components/filters/date-filter/date-filter.component';
import { RangeFilterComponent } from './components/filters/range-filter/range-filter.component';
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from "@angular/material/icon";
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import { MapComponent } from './components/shared/map/map.component';
import { LinkedStatComponent } from './components/shared/linked-stat/linked-stat.component';
import { StatComponent } from './components/shared/stat/stat.component';
import { SummationComponent } from './components/shared/summation/summation.component';
import { ChartComponent } from './components/shared/chart/chart.component';
import { DataViewTableComponent } from './components/shared/data-view-table/data-view-table.component';
import { DateFiltersComponent } from './components/shared/date-filters/date-filters.component';
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatOptionModule} from "@angular/material/core";
import {MatSelectModule} from "@angular/material/select";
import {MatDatepickerModule} from "@angular/material/datepicker";
import {MatNativeDateModule} from "@angular/material/core";
import {MatInputModule} from "@angular/material/input";
import {MatGridListModule} from "@angular/material/grid-list";
import {FlexModule} from "@angular/flex-layout";
import {MatTableModule} from "@angular/material/table";

@NgModule({
  declarations: [
    AppComponent,
    DataViewerComponent,
    SidebarComponent,
    HomeComponent,
    InputFilterComponent,
    MultiSelectFilterComponent,
    DateFilterComponent,
    RangeFilterComponent,
    MapComponent,
    LinkedStatComponent,
    StatComponent,
    SummationComponent,
    ChartComponent,
    DataViewTableComponent,
    DateFiltersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    HttpClientModule,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatOptionModule,
    MatSelectModule,
    MatDatepickerModule,
    MatInputModule,
    MatGridListModule,
    MatNativeDateModule,
    FlexModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
