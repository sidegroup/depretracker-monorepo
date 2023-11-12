Rails.application.routes.draw do
  resources :file_translations
  resources :line_translations do
    resources :review, only: [:new, :create] do
    end
  end

  resources :user_files do
    member do
      post :translate
    end
  end

end
