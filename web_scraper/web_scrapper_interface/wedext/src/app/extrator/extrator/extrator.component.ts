import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ExtratorService } from '../../service/extrator.service';
import { SnackService } from '../../service/snack.service';

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
    private snackBar: SnackService
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
         this.snackBar.showSuccess('Extração Reddit realizada!');
         this.loading = false;
         this.router.navigate(['/dataset']);
      },
      error: (err) => {
        if (err.status === 404) {
          this.snackBar.showErrorByStatus(err.status, err.error?.error || 'Subreddit não encontrado');
        }
        else {
          this.snackBar.showErrorByStatus(err.status);
        }
        this.loading = false;
      }
    });
  }

  private submitInstagramForm() {
    if (this.instagramForm.invalid) return;

    this.loading = true;
    this.extratorService.enviarDadosInstagram(this.instagramForm.value).subscribe({
      next: (res) => {
        this.snackBar.showSuccess('Extração Instagram realizada!');
        this.router.navigate(['/dataset']);
      },
      error: (err) => this.handleError(err, 'Instagram')
    });
  }

private handleError(err: any, platform: string) {
  console.error(err);
  const status = err.status || 0;
  this.snackBar.showErrorByStatus(
    status,
    `Erro na extração do ${platform}`
  );
  this.loading = false;
}
}
