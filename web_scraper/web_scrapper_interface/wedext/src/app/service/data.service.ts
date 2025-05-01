import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from "../../environments/environment.development";

@Injectable({
  providedIn: 'root'
})
export class DataService {
   private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getSubmissions(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/dados/submissoes`);
  }

  getComments(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/dados/comentarios`);
  }

  exportSubmissions(format: 'csv' | 'json'): Observable<Blob | any[]> {
    if (format === 'csv') {
      return this.http.get(`${this.apiUrl}/exportar/submissoes/csv`, {
        responseType: 'blob'
      });
    } else {
      return this.http.get<any[]>(`${this.apiUrl}/exportar/submissoes/json`);
    }
  }
  exportComments(format: 'csv' | 'json'): Observable<Blob | any[]> {
    if (format === 'csv') {
      return this.http.get(`${this.apiUrl}/exportar/comentarios/csv`, {
        responseType: 'blob'
      });
    } else {
      return this.http.get<any[]>(`${this.apiUrl}/exportar/comentarios/json`);
    }
  }
}
