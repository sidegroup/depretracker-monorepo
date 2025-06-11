import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { DataService } from '../../service/data.service';
import {MatPaginator, PageEvent} from '@angular/material/paginator';
import { MatSnackBar } from '@angular/material/snack-bar';
import { SnackService } from '../../service/snack.service';

@Component({
  selector: 'app-dataset',
  templateUrl: './dataset.component.html',
  styleUrls: ['./dataset.component.css', './fix-button-toggle.css']
})
export class DatasetComponent implements OnInit, AfterViewInit {
  submissionsColumns: string[] = ['post_id', 'title', 'date', 'text'];
  commentsColumns: string[] = ['id', 'post_id', 'date', 'body'];

  currentPage = 0;
  pageSize = 10;
  totalItems = 0;

  submissions: any[] = [];
  comments: any[] = [];

  submissionsTotal = 0;
  commentsTotal = 0;

  isLoading = false;

  counts = {
    submissions: 0,
    comments: 0
  };

  selectedDataType: 'submissions' | 'comments' = 'submissions';
  selectedFormat: 'csv' | 'json' = 'csv';

  @ViewChild('submissionsPaginator') submissionsPaginator!: MatPaginator;
  @ViewChild('commentsPaginator') commentsPaginator!: MatPaginator;

  constructor(
    private dataService: DataService,
    private snackService: SnackService
  ) {}

   ngOnInit(): void {
     this.loadData();
  }
  ngAfterViewInit(): void {
  // Garantindo a interface para proximas implementacoes
}
  loadData(): void {
  this.isLoading = true;

  if (this.selectedDataType === 'submissions') {
    this.dataService.getSubmissions(this.currentPage + 1, this.pageSize).subscribe({
      next: (response) => {
        this.submissions = response.data || [];
        this.submissionsTotal = response.total || 0;
        this.isLoading = false;
      },
      error: (err) => {
        this.isLoading = false;
        if (err.status === 404) {
          this.resetToFirstPage('submissions');
        } else {
          this.handleError('Nenhuma postagem disponível', err);
        }
      }
    });
  } else {
    this.dataService.getComments(this.currentPage + 1, this.pageSize).subscribe({
      next: (response) => {
        this.comments = response.data || [];
        this.commentsTotal = response.total || 0;
        this.isLoading = false;
      },
      error: (err) => {
        this.isLoading = false;
        if (err.status === 404) {
          this.resetToFirstPage('comments');
        } else {
          this.handleError('Nenhum comentário disponível', err);
        }
      }
    });
  }
}

private resetToFirstPage(dataType: 'submissions' | 'comments'): void {
  this.currentPage = 0;
  this.snackService.showError(`Página inválida. Voltando para a primeira página.`);

  // Atualizar o paginador visual
  if (dataType === 'submissions' && this.submissionsPaginator) {
    this.submissionsPaginator.firstPage();
  } else if (this.commentsPaginator) {
    this.commentsPaginator.firstPage();
  }

  this.loadData();
}
  onPageChange(event: PageEvent): void {
  this.currentPage = event.pageIndex;
  this.pageSize = event.pageSize;
  this.loadData();
  this.scrollToTop();
}
onDataTypeChange(newType: 'submissions' | 'comments'): void {
  if (this.selectedDataType !== newType) {
    this.selectedDataType = newType;
    this.currentPage = 0;
    this.loadData();
    this.scrollToTop();
  }
}
  get totalLength(): number {
  return this.selectedDataType === 'submissions'
    ? this.submissionsTotal
    : this.commentsTotal;
}
  private scrollToTop(): void {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }

  export(dataType: 'submissions' | 'comments', format: 'csv' | 'json'): void {
    const service$ = dataType === 'submissions'
      ? this.dataService.exportSubmissions(format)
      : this.dataService.exportComments(format);

    service$.subscribe({
      next: (data) => {
        const filename = `${dataType}_${this.getTimestamp()}.${format}`;
        if (format === 'csv') {
          this.downloadFile(data as Blob, filename);
           this.snackService.showSuccess(`Dados exportados como ${format.toUpperCase()}!`);
        } else {
          const jsonBlob = new Blob(
            [JSON.stringify(data, null, 2)],
            { type: 'application/json' }
          );
          this.downloadFile(jsonBlob, filename);
          this.snackService.showSuccess(`Dados exportados como ${format.toUpperCase()}!`);
        }
      },
      error: (err) => this.handleError('Erro na exportação', err)
    });
  }

  private getTimestamp(): string {
    return new Date().toISOString().replace(/[:.]/g, '-');
  }

  private downloadFile(blob: Blob, filename: string): void {
    const url = window.URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;
    anchor.click();
    window.URL.revokeObjectURL(url);
  }
  private handleError(context: string, error: any): void {
    console.error(context, error);
    const status = error?.status || 0;
    this.snackService.showErrorByStatus(status, context);
  }

}
