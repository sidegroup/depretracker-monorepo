import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {environment} from "../../environments/environment.development";

@Injectable({
  providedIn: 'root'
})
export class ExtratorService {

  private apiUrl = environment.apiUrl+'/crawl';

  constructor(private http: HttpClient) {}

 enviarDadosReddit(dados: any) {
   return this.http.post(this.apiUrl, dados, {
     headers: {'Content-Type': 'application/json'}
   });
 }

 //EM CONSTRUÇAO
  enviarDadosInstagram(dados: any) {
    return this.http.post(this.apiUrl, dados, {
      headers: {'Content-Type': 'application/json'}
    });
  }
}
