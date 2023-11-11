Rails.application.routes.draw do
  resources :user_files
  resources :examples do
    resources :review, only: [:new, :create] do
    end
  end

  resources :user_files do

  end

  resources :translations do

  end
end
