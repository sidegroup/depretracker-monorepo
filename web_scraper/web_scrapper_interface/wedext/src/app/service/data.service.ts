import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from "../../environments/environment.development";

@Injectable({
  providedIn: 'root'
})
export class DataService {
   private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

getSubmissions(page: number, pageSize: number): Observable<{data: any[], total: number}> {
  const params = new HttpParams()
    .set('page', page.toString())
    .set('page_size', pageSize.toString());

  return this.http.get<{data: any[], total: number}>(`${this.apiUrl}/dados/submissoes`, { params });
}

getComments(page: number, pageSize: number): Observable<{data: any[], total: number}> {
  const params = new HttpParams()
    .set('page', page.toString())
    .set('page_size', pageSize.toString());

  return this.http.get<{data: any[], total: number}>(`${this.apiUrl}/dados/comentarios`, { params });
}
  getCounts(): Observable<{ submissions: number; comments: number }> {
  return this.http.get<{ submissions: number; comments: number }>(`${this.apiUrl}/dados/contagem`);
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
