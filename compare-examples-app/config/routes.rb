Rails.application.routes.draw do
  resources :examples do
    resources :review, only: [:new, :create] do

    end
  end
end
