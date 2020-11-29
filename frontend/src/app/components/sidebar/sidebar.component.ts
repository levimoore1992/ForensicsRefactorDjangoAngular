import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  links: any[] = [{link: '/REC', text: 'REC'}, {link: '/SRE', text: 'SRE'}];
  isLoggedIn: boolean = true;

  constructor() { }
  ngOnInit(): void {
  }

}
