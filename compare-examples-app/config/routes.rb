Rails.application.routes.draw do
  resources :examples do
    resources :review, only: [:index, :new] do

    end
  end
end
