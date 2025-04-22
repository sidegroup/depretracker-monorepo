import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ExtratorService } from '../../service/extrator.service';

@Component({
  selector: 'app-extrator',
  templateUrl: './extrator.component.html',
  styleUrl: './extrator.component.css'
})
export class ExtratorComponent {
  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private extratorService: ExtratorService
  ) {
    this.form = this.fb.group({
      client_id: ['', Validators.required],
      client_secret: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      user_agent: ['', Validators.required],
      search_string: ['', Validators.required],
      subreddits: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.form.valid) {
      this.extratorService.enviarDados(this.form.value).subscribe({
        next: (res) => console.log('Resposta do back:', res),
        error: (err) => console.error('Erro ao enviar:', err),
      });
    }
  }
}
