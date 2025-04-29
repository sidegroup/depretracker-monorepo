import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {environment} from "../../environments/environment.development";

@Injectable({
  providedIn: 'root'
})
export class ExtratorService {

  private apiUrl = environment.apiUrl+'/crawl';

  constructor(private http: HttpClient) {}

 enviarDados(dados: any) {
   return this.http.post(this.apiUrl, dados, {
     headers: {'Content-Type': 'application/json'}
   });
 }
}
