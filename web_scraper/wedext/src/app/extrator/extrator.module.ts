import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ExtratorComponent } from './extrator/extrator.component';

import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';





@NgModule({
  declarations: [
    ExtratorComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule
  ],
  exports: [
    ExtratorComponent
  ]
})
export class ExtratorModule { }
