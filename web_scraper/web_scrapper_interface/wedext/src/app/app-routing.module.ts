import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './layout/home/home.component';
import { DatasetComponent } from './dataset/dataset/dataset.component';
import { ExtratorComponent } from './extrator/extrator/extrator.component';
import {AboutComponent} from "./layout/about/about.component";
import {UserGuideComponent} from "./layout/user-guide/user-guide.component";




const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent
  },
  {
     path: 'dataset',
     component: DatasetComponent
  },
  {
    path: 'extrator',
    component: ExtratorComponent
  },
  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: 'user-guide',
    component: UserGuideComponent
  },

  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
