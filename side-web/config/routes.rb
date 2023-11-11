Rails.application.routes.draw do
  resources :translations do
    resources :review, only: [:new, :create] do
    end
  end

  resources :user_files do
    member do
      post :translate
    end
  end

end
