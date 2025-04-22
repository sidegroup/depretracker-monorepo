import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ExtratorService {

  private apiUrl = 'http://localhost:5000/crawl';

  constructor(private http: HttpClient) {}

  enviarDados(dados: any) {
    return this.http.post(this.apiUrl, dados);
  }
}
