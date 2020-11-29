import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkedStatComponent } from './linked-stat.component';

describe('LinkedStatComponent', () => {
  let component: LinkedStatComponent;
  let fixture: ComponentFixture<LinkedStatComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LinkedStatComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LinkedStatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
