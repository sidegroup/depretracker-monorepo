Rails.application.routes.draw do
  # Root to file_translations#index
  root 'line_translations#index'

  resources :languages
  resources :line_translations, only: [:index] do
    resources :review, only: [:new, :create] do
    end
  end

  get 'translate', to: 'translator#get'

  resources :file_translations, only: [:index, :show, :new, :create]
  resources :user_files
end
