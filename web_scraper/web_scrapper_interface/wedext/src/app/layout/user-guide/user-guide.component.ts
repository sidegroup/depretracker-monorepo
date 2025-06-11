import { Component } from '@angular/core';

@Component({
  selector: 'app-user-guide',
  templateUrl: './user-guide.component.html',
  styleUrl: './user-guide.component.css'
})
export class UserGuideComponent {
  /**
   * Abre uma imagem em uma nova janela ou guia
   * @param imagePath Caminho para a imagem a ser aberta
   */
  openImage(imagePath: string): void {
    // Abre a imagem em uma nova janela/guia
    window.open(imagePath, '_blank');
  }
}
