import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SummationComponent } from './summation.component';

describe('SummationComponent', () => {
  let component: SummationComponent;
  let fixture: ComponentFixture<SummationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SummationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SummationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
