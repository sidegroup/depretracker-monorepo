import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { MenuComponent } from './menu/menu.component';
import { FooterComponent } from './footer/footer.component';
import { MatSidenav } from '@angular/material/sidenav';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import {MatMenuModule, MatMenuTrigger} from "@angular/material/menu";
import {RouterLink} from "@angular/router";



@NgModule({
  declarations: [
    HomeComponent,
    MenuComponent,
    FooterComponent
  ],
  exports: [
    MenuComponent,
    FooterComponent
  ],
  
  imports: [
    CommonModule, 
    MatSidenav,
    MatToolbarModule, 
    MatButtonModule,
    MatCardModule,  
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatMenuTrigger,
    MatMenuModule,
    RouterLink
  ]
})
export class LayoutModule { }
