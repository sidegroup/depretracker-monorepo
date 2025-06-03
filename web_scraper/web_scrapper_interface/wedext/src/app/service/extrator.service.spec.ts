import { TestBed } from '@angular/core/testing';

import { ExtratorService } from './extrator.service';

describe('ExtratorService', () => {
  let service: ExtratorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ExtratorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
