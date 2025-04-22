import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { DataService } from '../../service/data.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-dataset',
  templateUrl: './dataset.component.html',
  styleUrls: ['./dataset.component.css']
})
export class DatasetComponent implements OnInit, AfterViewInit {
  // Configuração das tabelas
  submissionsColumns: string[] = ['id', 'author', 'title', 'created_utc'];
  commentsColumns: string[] = ['id', 'author', 'body', 'created_utc'];
  
  // Fontes de dados para as tabelas
  submissions = new MatTableDataSource<any>([]);
  comments = new MatTableDataSource<any>([]);
  
  // Estado de carregamento
  isLoading = true;

  selectedDataType: 'submissions' | 'comments' = 'submissions';
  selectedFormat: 'csv' | 'json' = 'csv';

  // Paginação
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  constructor(
    private dataService: DataService,
    private snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
    this.loadData();
  }

  ngAfterViewInit(): void {
    this.submissions.paginator = this.paginator;
    this.comments.paginator = this.paginator;
  }

  // Carrega os dados do backend
  loadData(): void {
    this.isLoading = true;
    
    this.dataService.getSubmissions().subscribe({
      next: (data) => {
        this.submissions.data = data;
      },
      error: (err) => this.handleError('Erro ao carregar postagens', err)
    });

    this.dataService.getComments().subscribe({
      next: (data) => {
        this.comments.data = data;
        this.isLoading = false;
      },
      error: (err) => {
        this.isLoading = false;
        this.handleError('Erro ao carregar comentários', err);
      }
    });
  }

  // Manipula a exportação de dados
  export(dataType: 'submissions' | 'comments', format: 'csv' | 'json'): void {
    const service$ = dataType === 'submissions' 
      ? this.dataService.exportSubmissions(format)
      : this.dataService.exportComments(format);

    service$.subscribe({
      next: (data) => {
        if (format === 'csv') {
          this.downloadFile(data as Blob, `${dataType}_${this.getTimestamp()}.csv`);
        } else {
          this.downloadFile(
            new Blob(
              [JSON.stringify(data, null, 2)], 
              { type: 'application/json' }
            ),
            `${dataType}_${this.getTimestamp()}.json`
          );
        }
      },
      error: (err) => this.handleError('Erro na exportação', err)
    });
  }

  // Gera timestamp para nome de arquivo
  private getTimestamp(): string {
    return new Date().toISOString().replace(/[:.]/g, '-');
  }

  // Método para download de arquivo
  private downloadFile(blob: Blob, filename: string): void {
    const url = window.URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;
    anchor.click();
    window.URL.revokeObjectURL(url);
  }

  // Exibe erros para o usuário
  private handleError(message: string, error: any): void {
    console.error(message, error);
    this.snackBar.open(
      `${message}: ${error.message || 'Erro desconhecido'}`,
      'Fechar', 
      { duration: 5000 }
    );
  }
}