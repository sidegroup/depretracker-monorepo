import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ExtratorService } from '../../service/extrator.service';

@Component({
  selector: 'app-extrator',
  templateUrl: './extrator.component.html',
  styleUrl: './extrator.component.css'
})
export class ExtratorComponent {
  redditForm: FormGroup;
  instagramForm: FormGroup;
  activeForm: 'reddit' | 'instagram' = 'reddit';
  loading = false;

  constructor(
    private fb: FormBuilder,
    private extratorService: ExtratorService,
    private router: Router,
    private snackBar: MatSnackBar
  ) {
    // Formulário Reddit
    this.redditForm = this.fb.group({
      client_id: ['', Validators.required],
      client_secret: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      user_agent: ['', Validators.required],
      search_string: ['', Validators.required],
      subreddits: ['', Validators.required],
    });

    // Formulário Instagram
    this.instagramForm = this.fb.group({
      app_id: ['', Validators.required],
      app_secret: ['', Validators.required],
      access_token: ['', Validators.required],
      account_id: ['', Validators.required],
      hashtags: [''],
      target_accounts: ['']
    });
  }

  onSubmit() {
    if (this.activeForm === 'reddit') {
      this.submitRedditForm();
    } else {
      this.submitInstagramForm();
    }
  }

  private submitRedditForm() {
    if (this.redditForm.invalid) return;

    this.loading = true;
    this.extratorService.enviarDadosReddit(this.redditForm.value).subscribe({
      next: (res) => {
        this.snackBar.open('Extração Reddit realizada!', 'Fechar', { duration: 3000 });
        this.router.navigate(['/dataset']);
      },
      error: (err) => this.handleError(err, 'Reddit')
    });
  }

  private submitInstagramForm() {
    if (this.instagramForm.invalid) return;

    this.loading = true;
    this.extratorService.enviarDadosInstagram(this.instagramForm.value).subscribe({
      next: (res) => {
        this.snackBar.open('Extração Instagram realizada!', 'Fechar', { duration: 3000 });
        this.router.navigate(['/dataset']);
      },
      error: (err) => this.handleError(err, 'Instagram')
    });
  }

  private handleError(err: any, platform: string) {
    console.error(err);
    let message = `Erro na extração do ${platform}`;
    if (err.status === 401 || err.status === 403) {
      message = 'Credenciais inválidas!';
    }
    this.snackBar.open(message, 'Fechar', { duration: 4000 });
    this.loading = false;
  }
}
