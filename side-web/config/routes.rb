Rails.application.routes.draw do
  resources :line_translations do
    resources :review, only: [:new, :create] do
    end
  end

  resources :file_translations
  resources :user_files
end
