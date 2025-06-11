import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class SnackService {
  constructor(private snackBar: MatSnackBar) {}

  showErrorByStatus(status: number, customMessage?: string): void {
    let message = '';

    switch (status) {
      case 404:
        message = customMessage || 'Subreddit não encontrado. Verifique o nome digitado.';
        break;
      case 401:
      case 403:
        message = 'Credenciais inválidas.';
        break;
      default:
        message = customMessage || 'Erro na extração dos dados.';
        break;
    }

    this.showError(message);
  }

  showError(message: string): void {
    this.snackBar.open(message, 'Fechar', {
      duration: 5000,
      panelClass: ['snackbar-error']
    });
  }

  showSuccess(message: string): void {
    this.snackBar.open(message, 'OK', {
      duration: 3000,
      panelClass: ['snackbar-success']
    });
  }

  showInfo(message: string): void {
    this.snackBar.open(message, 'Fechar', {
      duration: 4000,
      panelClass: ['snackbar-info']
    });
  }
}
