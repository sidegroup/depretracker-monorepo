Rails.application.routes.draw do
  resources :languages
  resources :line_translations do
    resources :review, only: [:new, :create] do
    end
  end

  resources :file_translations, only: [:index, :show, :new, :create]
  resources :user_files
end
